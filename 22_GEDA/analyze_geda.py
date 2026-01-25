import pandas as pd
import pyreadstat
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import os
import numpy as np

# Configuration
INPUT_FILE = 'GEDA19.sav'
OUTPUT_DIR = 'GEDA_Analysis_Results'

# Create output directory
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

print("Loading data...")
df, meta = pyreadstat.read_sav(INPUT_FILE)
print("Data loaded.")

# Helper function to get label
def get_label(col_name, val):
    if col_name in meta.variable_value_labels:
        return meta.variable_value_labels[col_name].get(val, val)
    return val

# Helper to map entire column to labels
def map_labels(series, col_name):
    if col_name in meta.variable_value_labels:
        return series.map(meta.variable_value_labels[col_name])
    return series

# Analysis 1: General Health (GZmehm1_k) vs Age (age10B) and Sex (sex)
# GZmehm1_k: 1=Sehr gut/gut, 2=Mittelmäßig/Schlecht/Sehr schlecht (Need to verify coding)
# Let's inspect unique values first for safety in a real scenario, but here we assume standard coding.
print("Running Analysis 1: Health by Age...")
try:
    sub = df[['age10B', 'sex', 'GZmehm1_k']].dropna()
    sub['age_label'] = map_labels(sub['age10B'], 'age10B')
    sub['sex_label'] = map_labels(sub['sex'], 'sex')
    sub['health_label'] = map_labels(sub['GZmehm1_k'], 'GZmehm1_k')
    
    # Cross tab
    ct = pd.crosstab(sub['age_label'], sub['health_label'], normalize='index') * 100
    
    # Stats
    chi2, p, dof, ex = stats.chi2_contingency(pd.crosstab(sub['age_label'], sub['health_label']))
    
    # Plot
    plt.figure(figsize=(10, 6))
    sns.heatmap(ct, annot=True, fmt=".1f", cmap="YlGnBu")
    plt.title("Prozentualer Anteil nach Gesundheitszustand und Alter")
    plt.ylabel("Altersgruppe")
    plt.xlabel("Selbsteingeschätzte Gesundheit")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/01_Health_Age_Heatmap.png")
    plt.close()

    # Write MD
    with open(f"{OUTPUT_DIR}/01_Gesundheit_Alter.md", "w", encoding="utf-8") as f:
        f.write("# Analyse 1: Subjektive Gesundheit nach Alter\n\n")
        f.write("## Fragestellung\nWie verändert sich die subjektive Gesundheit mit dem Alter?\n\n")
        f.write("## Ergebnisse\n")
        f.write(ct.to_markdown())
        f.write(f"\n\n**Statistik:**\n- Chi-Quadrat: {chi2:.2f}\n- p-Wert: {p:.4e}\n")
        f.write("Interpretation: Ein p-Wert < 0.05 zeigt einen signifikanten Zusammenhang.\n\n")
        f.write("![Grafik](01_Health_Age_Heatmap.png)\n")

except Exception as e:
    print(f"Error in Analysis 1: {e}")

# Analysis 2: BMI (PAbmiB_k) vs Education (SDisced11)
print("Running Analysis 2: BMI by Education...")
try:
    sub = df[['SDisced11', 'PAbmiB_k']].dropna()
    sub = sub[sub['SDisced11'] > 0] # Filter out invalid codes if any negative
    sub['edu_label'] = map_labels(sub['SDisced11'], 'SDisced11')
    sub['bmi_label'] = map_labels(sub['PAbmiB_k'], 'PAbmiB_k')
    
    ct = pd.crosstab(sub['edu_label'], sub['bmi_label'], normalize='index') * 100
    chi2, p, dof, ex = stats.chi2_contingency(pd.crosstab(sub['edu_label'], sub['bmi_label']))

    plt.figure(figsize=(12, 6))
    ct.plot(kind='bar', stacked=True, colormap='viridis', figsize=(10,6))
    plt.title("BMI Gruppen nach Bildungsstand")
    plt.ylabel("Anteil (%)")
    plt.xlabel("Bildung (ISCED)")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/02_BMI_Education_Bar.png")
    plt.close()

    with open(f"{OUTPUT_DIR}/02_BMI_Bildung.md", "w", encoding="utf-8") as f:
        f.write("# Analyse 2: BMI und Bildung\n\n")
        f.write("## Fragestellung\nGibt es einen sozialen Gradienten beim Übergewicht?\n\n")
        f.write("## Ergebnisse\n")
        f.write(ct.to_markdown())
        f.write(f"\n\n**Statistik:**\n- Chi-Quadrat: {chi2:.2f}\n- p-Wert: {p:.4e}\n")
        f.write("![Grafik](02_BMI_Education_Bar.png)\n")
except Exception as e:
    print(f"Error in Analysis 2: {e}")


# Analysis 3: Smoking (RCstatE_k3) vs Depression (PKdep12)
print("Running Analysis 3: Smoking and Depression...")
try:
    # Check variable names again. PKdep12 might be 1=Ja, 2=Nein. RCstatE_k3 might be 1=Raucher, 2=Nichtraucher
    sub = df[['RCstatE_k3', 'PKdep12']].dropna()
    # Assuming positive values are valid responses
    sub = sub[(sub['RCstatE_k3'] > 0) & (sub['PKdep12'] > 0)]
    
    sub['smoker_label'] = map_labels(sub['RCstatE_k3'], 'RCstatE_k3')
    sub['dep_label'] = map_labels(sub['PKdep12'], 'PKdep12')

    ct_count = pd.crosstab(sub['smoker_label'], sub['dep_label'])
    ct_norm = pd.crosstab(sub['smoker_label'], sub['dep_label'], normalize='index') * 100
    
    chi2, p, dof, ex = stats.chi2_contingency(ct_count)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(ct_norm, annot=True, fmt=".1f", cmap="Reds")
    plt.title("Rauchen und Depression (12 Monate)")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/03_Smoking_Depression.png")
    plt.close()

    with open(f"{OUTPUT_DIR}/03_Rauchen_Depression.md", "w", encoding="utf-8") as f:
        f.write("# Analyse 3: Rauchen und Depression\n\n")
        f.write("## Fragestellung\nRauchen Menschen mit Depression häufiger?\n\n")
        f.write("## Tabelle (Prozent)\n")
        f.write(ct_norm.to_markdown())
        f.write(f"\n\n**Statistik:**\n- Chi-Quadrat: {chi2:.2f}\n- p-Wert: {p:.4e}\n")
        f.write("![Grafik](03_Smoking_Depression.png)\n")

except Exception as e:
    print(f"Error in Analysis 3: {e}")


# Analysis 4: Physical Activity (KAgfka) vs Chronic Diseases (GZmehm3C)
print("Running Analysis 4: Physical Activity vs Chronic Diseases...")
try:
    sub = df[['KAgfka', 'GZmehm3C']].dropna()
    sub = sub[(sub['KAgfka'] >= 0) & (sub['GZmehm3C'] >= 0)]
    
    sub['activity_label'] = map_labels(sub['KAgfka'], 'KAgfka')
    sub['chronic_label'] = map_labels(sub['GZmehm3C'], 'GZmehm3C') # 1=Yes, 0/2=No typically

    ct = pd.crosstab(sub['activity_label'], sub['chronic_label'], normalize='index') * 100
    chi2, p, dof, ex = stats.chi2_contingency(pd.crosstab(sub['activity_label'], sub['chronic_label']))

    plt.figure(figsize=(8, 6))
    ct.plot(kind='bar', stacked=True)
    plt.title("Chronische Krankheit nach WHO-Aktivitätsempfehlung")
    plt.ylabel("Anteil (%)")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/04_Activity_Chronic.png")
    plt.close()

    with open(f"{OUTPUT_DIR}/04_Bewegung_Chronisch.md", "w", encoding="utf-8") as f:
        f.write("# Analyse 4: Bewegung und Chronische Krankheiten\n\n")
        f.write("## Fragestellung\nHaben Menschen, die sich genug bewegen, weniger chronische Krankheiten?\n\n")
        f.write(ct.to_markdown())
        f.write(f"\n\n**Statistik:**\n- Chi-Quadrat: {chi2:.2f}\n- p-Wert: {p:.4e}\n")
        f.write("![Grafik](04_Activity_Chronic.png)\n")

except Exception as e:
    print(f"Error in Analysis 4: {e}")

# Analysis 5: Unmet Medical Need (IAkosten) vs Income (SDhhincome)
print("Running Analysis 5: Unmet Need vs Income...")
try:
    sub = df[['IAkosten', 'SDhhincome']].dropna()
    sub = sub[(sub['IAkosten'] >= 0) & (sub['SDhhincome'] > 0)]
    
    sub['cost_barrier'] = map_labels(sub['IAkosten'], 'IAkosten')
    sub['income_quintile'] = map_labels(sub['SDhhincome'], 'SDhhincome')
    
    ct = pd.crosstab(sub['income_quintile'], sub['cost_barrier'], normalize='index') * 100
    
    # Check if 'cost_barrier' has a "Yes" category to focus on
    # Plotting full stack
    plt.figure(figsize=(10, 6))
    ct.plot(kind='bar', stacked=True, colormap='RdYlGn')
    plt.title("Verzicht auf Arztbesuch aus Kostengründen nach Einkommen")
    plt.ylabel("Anteil (%)")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/05_Cost_Income.png")
    plt.close()
    
    chi2, p, dof, ex = stats.chi2_contingency(pd.crosstab(sub['income_quintile'], sub['cost_barrier']))

    with open(f"{OUTPUT_DIR}/05_Kosten_Einkommen.md", "w", encoding="utf-8") as f:
        f.write("# Analyse 5: Arztbesuch-Verzicht aus Kostengründen\n\n")
        f.write("## Fragestellung\nVerzichten ärmere Menschen häufiger auf Arztbesuche aus Geldmangel?\n\n")
        f.write(ct.to_markdown())
        f.write(f"\n\n**Statistik:**\n- Chi-Quadrat: {chi2:.2f}\n- p-Wert: {p:.4e}\n")
        f.write("![Grafik](05_Cost_Income.png)\n")

except Exception as e:
    print(f"Error in Analysis 5: {e}")

print("Analysis complete.")
