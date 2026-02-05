import sqlite3
import datetime
import os
import sys

# Konfiguration
DB_FILE = 'tracker.db'
OBSIDIAN_STATS_FILE = '../TRACKER_STATS.md' # Relativer Pfad zum Obsidian Root
USER_PROFILE = {
    "name": "Andreas",
    "age": 26,
    "gender": "male",
    "height_cm": 180, # Annahme, bitte korrigieren wenn nötig
    "weight_kg": 93.0, # Startwert Q1
    "activity_level": 1.55, # Moderat bis Aktiv (6x Training)
    "goal_calories": 3200, # Massephase Ziel
    "goal_protein": 200, # 2g/kg
    "goal_water_ml": 3500
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
## ℹ️ Info
* **Startgewicht:** {USER_PROFILE['weight_kg']} kg
* **Grundumsatz (BMR):** {bmr} kcal
* **Erhaltungskalorien (TDEE):** {tdee} kcal
* **Masse-Ziel:** {goal_cal} kcal (+{(goal_cal - tdee)} Surplus)

"""
    # Letzte 7 Tage Tabelle
    md_content += "
## 🗓️ Letzte 7 Tage
"
    md_content += "| Datum | Kcal | Protein | Wasser | Gewicht |
"
    md_content += "|---|---|---|---|---|
"
    
    start_date = datetime.date.today() - datetime.timedelta(days=6)
    c.execute("SELECT date, calories, protein, water_ml, weight_kg FROM daily_logs WHERE date >= ? ORDER BY date DESC", (start_date.isoformat(),))
    rows = c.fetchall()
    
    for r in rows:
        d, c_val, p_val, w_val, kg_val = r
        kg_display = f"{kg_val} kg" if kg_val else "-"
        md_content += f"| {d} | {c_val} | {p_val}g | {w_val}ml | {kg_display} |
"

    with open(OBSIDIAN_STATS_FILE, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"📄 Obsidian Dashboard aktualisiert: {OBSIDIAN_STATS_FILE}")
    conn.close()

def main():
    init_db()
    
    print("--- 🏋️ FIT TRACKER CLI 🏋️ ---")
    print("1. Essen tracken (Kcal/Protein)")
    print("2. Wasser tracken")
    print("3. Körperdaten (Gewicht/KFA)")
    print("4. Dashboard aktualisieren")
    print("q. Beenden")
    
    choice = input("Wahl: ")
    today = datetime.date.today().isoformat()
    
    if choice == "1":
        kcal = int(input("Kalorien (kcal): ") or 0)
        prot = int(input("Protein (g): ") or 0)
        log_data(today, calories=kcal, protein=prot)
        
    elif choice == "2":
        ml = int(input("Wasser (ml): ") or 0)
        log_data(today, water_ml=ml)
        
    elif choice == "3":
        kg = float(input("Gewicht (kg): ") or 0)
        kfa = float(input("Körperfett (%): ") or 0)
        # Gewicht überschreiben wir meist als 'aktuellen Stand'
        log_data(today, weight_kg=kg, body_fat_percent=kfa)
        # TODO: Hier könnte der Google Fit Sync Hook sein
        
    elif choice == "4":
        generate_obsidian_dashboard()
        
    if choice in ["1", "2", "3"]:
        generate_obsidian_dashboard() # Auto-Update nach Eingabe

if __name__ == "__main__":
    main()
