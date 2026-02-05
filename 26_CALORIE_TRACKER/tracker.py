import sqlite3
import datetime
import os
import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Konfiguration
DB_FILE = 'tracker.db'
OBSIDIAN_STATS_FILE = '../TRACKER_STATS.md' # Relativer Pfad zum Obsidian Root
CHART_FILE = 'progress_chart.png'
USER_PROFILE = {
    "name": "Andreas",
    "age": 26,
    "gender": "male",
    "height_cm": 180, 
    "weight_kg": 93.0, 
    "activity_level": 1.55, 
    "goal_calories": 3200, 
    "goal_protein": 200, 
    "goal_water_ml": 3500
}

# Standard-Nahrungsmittel (Name: [Kcal, Protein])
FOOD_PRESETS = {
    "1": ("Magerquark (500g)", 340, 60),
    "2": ("Reis (100g roh)", 350, 7),
    "3": ("Hähnchenbrust (200g)", 220, 46),
    "4": ("Protein Shake (30g)", 110, 24),
    "5": ("Haferflocken (100g)", 370, 13),
    "6": ("Eier (3 Stück)", 240, 21),
    "7": ("Banane", 100, 1)
}

def init_db():
    """Initialisiert die Datenbank falls nicht vorhanden."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    # Tabelle für tägliche Logs
    c.execute('''CREATE TABLE IF NOT EXISTS daily_logs (
        date TEXT PRIMARY KEY,
        calories INTEGER DEFAULT 0,
        protein INTEGER DEFAULT 0,
        carbs INTEGER DEFAULT 0,
        fats INTEGER DEFAULT 0,
        water_ml INTEGER DEFAULT 0,
        weight_kg REAL,
        body_fat_percent REAL,
        notes TEXT
    )''')
    
    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect(DB_FILE)

def calculate_tdee():
    """Berechnet Grundumsatz und Gesamtumsatz."""
    # Mifflin-St Jeor Formel
    p = USER_PROFILE
    if p["gender"] == "male":
        bmr = (10 * p["weight_kg"]) + (6.25 * p["height_cm"]) - (5 * p["age"]) + 5
    else:
        bmr = (10 * p["weight_kg"]) + (6.25 * p["height_cm"]) - (5 * p["age"]) - 161
        
    tdee = bmr * p["activity_level"]
    return int(bmr), int(tdee)

def log_data(date, **kwargs):
    """Loggt Daten für einen bestimmten Tag (Update oder Insert)."""
    conn = get_connection()
    c = conn.cursor()
    
    # Prüfen ob Eintrag existiert
    c.execute("SELECT * FROM daily_logs WHERE date=?", (date,))
    exists = c.fetchone()
    
    if not exists:
        c.execute("INSERT INTO daily_logs (date) VALUES (?)", (date,))
    
    # Dynamisches Update Query
    for key, value in kwargs.items():
        if value is not None:
            # Für Kalorien/Makros/Wasser addieren wir, für Gewicht überschreiben wir?
            # Hier: Einfache Logik -> Wir addieren bei Nutrition, überschreiben bei Body stats.
            if key in ['calories', 'protein', 'carbs', 'fats', 'water_ml']:
                c.execute(f"UPDATE daily_logs SET {key} = {key} + ? WHERE date=?", (value, date))
            else:
                c.execute(f"UPDATE daily_logs SET {key} = ? WHERE date=?", (value, date))
                
    conn.commit()
    conn.close()
    print(f"✅ Daten für {date} gespeichert.")

def create_charts():
    """Erstellt ein Verlaufsdiagramm."""
    conn = get_connection()
    # Letzte 30 Tage abrufen
    start_date = datetime.date.today() - datetime.timedelta(days=30)
    query = "SELECT date, weight_kg, calories FROM daily_logs WHERE date >= ? ORDER BY date ASC"
    df = conn.execute(query, (start_date.isoformat(),)).fetchall()
    conn.close()

    if not df:
        return

    dates = [datetime.datetime.strptime(x[0], "%Y-%m-%d") for x in df]
    weights = [x[1] for x in df]
    calories = [x[2] for x in df]

    # Nur plotten, wenn Daten vorhanden sind
    if not any(weights) and not any(calories):
        return

    fig, ax1 = plt.subplots(figsize=(10, 5))
    
    # Style
    plt.style.use('ggplot')
    
    # Achse 1: Gewicht
    color = 'tab:red'
    ax1.set_xlabel('Datum')
    ax1.set_ylabel('Gewicht (kg)', color=color)
    # Filtere None values für Plot
    clean_dates_w = [d for d, w in zip(dates, weights) if w]
    clean_weights = [w for w in weights if w]
    if clean_weights:
        ax1.plot(clean_dates_w, clean_weights, color=color, marker='o', label='Gewicht')
        ax1.tick_params(axis='y', labelcolor=color)

    # Achse 2: Kalorien
    ax2 = ax1.twinx()  
    color = 'tab:blue'
    ax2.set_ylabel('Kalorien (kcal)', color=color)  
    ax2.bar(dates, calories, color=color, alpha=0.3, label='Kalorien')
    ax2.tick_params(axis='y', labelcolor=color)
    
    # Ziellinie Kalorien
    ax2.axhline(y=USER_PROFILE["goal_calories"], color='green', linestyle='--', alpha=0.5, label='Ziel')

    fig.tight_layout()  
    plt.title('Gewichtsverlauf & Kalorienaufnahme')
    
    # Speichern im Tracker Ordner
    plt.savefig(CHART_FILE)
    plt.close()
    print("📊 Diagramm aktualisiert.")

def generate_obsidian_dashboard():
    """Erstellt eine Markdown-Datei mit Statistiken für Obsidian."""
    conn = get_connection()
    c = conn.cursor()
    
    today = datetime.date.today().isoformat()
    c.execute("SELECT * FROM daily_logs WHERE date=?", (today,))
    row = c.fetchone()
    
    # Defaults
    cal, prot, water = 0, 0, 0
    if row:
        # Indexmapping basierend auf CREATE TABLE
        cal = row[1]
        prot = row[2]
        water = row[5]
    
    bmr, tdee = calculate_tdee()
    goal_cal = USER_PROFILE["goal_calories"]
    
    # Chart erstellen
    create_charts()

    # Fortschrittsbalken Logik (ASCII style für Markdown)
    def progress_bar(current, total, length=20):
        percent = min(1.0, current / total) if total > 0 else 0
        filled = int(length * percent)
        bar = "▓" * filled + "░" * (length - filled)
        return f"{bar} {int(percent*100)}%"

    md_content = f"""# 📊 Fitness Tracker Stats
*Aktualisiert: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}*

## 📅 Heute ({today})

**Kalorien** (Ziel: {goal_cal} kcal)
{progress_bar(cal, goal_cal)}
**{cal}** / {goal_cal} kcal | Bilanz: {cal - tdee} kcal (vs TDEE)

**Protein** (Ziel: {USER_PROFILE['goal_protein']}g)
{progress_bar(prot, USER_PROFILE['goal_protein'])}
**{prot}g** / {USER_PROFILE['goal_protein']}g

**Wasser** (Ziel: {USER_PROFILE['goal_water_ml']}ml)
{progress_bar(water, USER_PROFILE['goal_water_ml'])}
**{water}ml** / {USER_PROFILE['goal_water_ml']}ml

---
## 📈 Verlauf
![Verlauf](26_CALORIE_TRACKER/{CHART_FILE})

---
## ℹ️ Info
* **Startgewicht:** {USER_PROFILE['weight_kg']} kg
* **Grundumsatz (BMR):** {bmr} kcal
* **Erhaltungskalorien (TDEE):** {tdee} kcal
* **Masse-Ziel:** {goal_cal} kcal (+{(goal_cal - tdee)} Surplus)

"""
    # Letzte 7 Tage Tabelle
    md_content += "\n## 🗓️ Letzte 7 Tage\n"
    md_content += "| Datum | Kcal | Protein | Wasser | Gewicht |\n"
    md_content += "|---|---|---|---|---|\n"
    
    start_date = datetime.date.today() - datetime.timedelta(days=6)
    c.execute("SELECT date, calories, protein, water_ml, weight_kg FROM daily_logs WHERE date >= ? ORDER BY date DESC", (start_date.isoformat(),))
    rows = c.fetchall()
    
    for r in rows:
        d, c_val, p_val, w_val, kg_val = r
        kg_display = f"{kg_val} kg" if kg_val else "-"
        md_content += f"| {d} | {c_val} | {p_val}g | {w_val}ml | {kg_display} |\n"

    with open(OBSIDIAN_STATS_FILE, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"📄 Obsidian Dashboard aktualisiert: {OBSIDIAN_STATS_FILE}")
    conn.close()

def main():
    init_db()
    
    print("--- 🏋️ FIT TRACKER CLI 🏋️ ---")
    print("1. Essen tracken (Manuell)")
    print("2. Essen tracken (Presets)")
    print("3. Wasser tracken")
    print("4. Körperdaten (Gewicht/KFA)")
    print("5. Dashboard aktualisieren")
    print("q. Beenden")
    
    choice = input("Wahl: ")
    today = datetime.date.today().isoformat()
    
    if choice == "1":
        kcal = int(input("Kalorien (kcal): ") or 0)
        prot = int(input("Protein (g): ") or 0)
        log_data(today, calories=kcal, protein=prot)
    
    elif choice == "2":
        print("\n--- 🍎 Presets ---")
        for k, v in FOOD_PRESETS.items():
            print(f"{k}. {v[0]} ({v[1]} kcal, {v[2]}g Protein)")
        
        p_choice = input("Nummer wählen: ")
        if p_choice in FOOD_PRESETS:
            name, kcal, prot = FOOD_PRESETS[p_choice]
            print(f"Adding: {name}")
            log_data(today, calories=kcal, protein=prot)
        else:
            print("Ungültige Wahl.")

    elif choice == "3":
        ml = int(input("Wasser (ml): ") or 250)
        log_data(today, water_ml=ml)
        
    elif choice == "4":
        kg = float(input("Gewicht (kg): ") or 0)
        kfa = float(input("Körperfett (%): ") or 0)
        # Gewicht überschreiben wir meist als 'aktuellen Stand'
        log_data(today, weight_kg=kg, body_fat_percent=kfa)
        
    elif choice == "5":
        generate_obsidian_dashboard()
        
    if choice in ["1", "2", "3", "4"]:
        generate_obsidian_dashboard() # Auto-Update nach Eingabe

if __name__ == "__main__":
    main()