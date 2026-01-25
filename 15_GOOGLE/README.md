# 🛠️ Google Script Utilities & API Dokumentation

Dieses Repository enthält eine Sammlung von Python-Skripten zur Interaktion mit verschiedenen Google-Diensten (Gmail, Drive, Tasks, Fit).

## 🚀 Schnellstart

### Voraussetzungen
1.  Python 3.10+
2.  Ein aktives Google Cloud Projekt mit konfiguriertem OAuth Consent Screen.
3.  `credentials_desktop.json` (oder `key_neu.json`) im Projektverzeichnis.

### Installation

Alle Abhängigkeiten werden in einer virtuellen Umgebung verwaltet:

```bash
# Virtuelle Umgebung aktivieren (Windows)
.\.venv\Scripts\activate

# Abhängigkeiten installieren
pip install -r requirements.json
```

### Authentifizierung

Die Authentifizierung erfolgt über OAuth2. Beim ersten Start oder wenn neue Berechtigungen hinzugefügt wurden, muss der Login erneuert werden:

```bash
python login_fix.py
```

Dies öffnet ein Browserfenster, in dem du den Zugriff bestätigen musst. Das resultierende Token wird in `token.json` gespeichert.

---

## 📂 Skript-Übersicht

### 1. Google Drive (`drive_client.py`)
Verwaltet Dateien und Speicherplatz.

**Funktionen:**
*   **Letzte Dateien:** Listet die 20 zuletzt bearbeiteten Dateien auf.
*   **Suche:** Durchsucht Drive nach Dateinamen.
*   **Speicheranalyse:** Ermittelt Gesamtspeicherverbrauch und die Top 10 größten Dateien. Exportiert diese in `drive_analysis.csv`.

**Nutzung:**
```bash
# Startet interaktives Menü
python drive_client.py

# Direktstart der Analyse
python drive_client.py analyze
```

### 2. Gmail (`gmail_client.py`)
Liest und sendet E-Mails.

**Funktionen:**
*   **Posteingang:** Listet ungelesene Nachrichten oder E-Mails von heute.
*   **Lesen:** Zeigt den Textinhalt einer E-Mail an.
*   **Senden:** Versendet einfache Text-E-Mails.

**Nutzung:**
```bash
python gmail_client.py
```

### 3. Google Tasks (`check_tasks.py`)
Liest To-Do Listen aus.

**Funktionen:**
*   **Listen:** Zeigt alle Task-Listen an.
*   **Aufgaben:** Listet offene und erledigte Aufgaben inklusive Notizen.

**Nutzung:**
```bash
python check_tasks.py
```

### 4. Google Fit (`fit_client.py`)
Liest Gesundheitsdaten aus.

**Funktionen:**
*   **Schritte:** Aggregiert die Schritte der letzten 7 Tage.

**Nutzung:**
```bash
python fit_client.py
```

---

## 🔌 API Referenz

Folgende APIs und Scopes werden verwendet:

### Verwendete Scopes (`auth_helper.py`)
| Dienst | Scope URL | Zweck |
| :--- | :--- | :--- |
| **Gmail** | `.../gmail.modify` | Mails lesen/löschen/verändern |
| **Gmail** | `.../gmail.send` | Mails senden |
| **Drive** | `.../drive.readonly` | Metadaten & Inhalte lesen |
| **Docs** | `.../documents.readonly` | Google Docs Inhalte lesen |
| **Tasks** | `.../tasks.readonly` | Aufgaben lesen |
| **Fit** | `.../fitness.activity.read` | Aktivitätsdaten (Schritte) |
| **Fit** | `.../fitness.body.read` | Körperdaten |
| **Fit** | `.../fitness.sleep.read` | Schlafdaten |
| **Fit** | `.../fitness.heart_rate.read` | Herzfrequenz |

### Endpunkte & Methoden

#### Drive API v3
*   `files().list(q=..., orderBy=..., fields=...)`: Suchen und Auflisten von Dateien.
    *   Wichtig für Analyse: `orderBy='quotaBytes desc'` für Sortierung nach Größe.
*   `about().get(fields='storageQuota')`: Abrufen des Gesamtspeichers.

#### Gmail API v1
*   `users().messages().list(userId='me', q=...)`: Suchen von Nachricht-IDs.
*   `users().messages().get(...)`: Abrufen von Metadaten (Header) oder vollem Inhalt (`format='full'`).
*   `users().messages().send(...)`: Versenden von RFC 2822 kodierten Nachrichten.

#### Tasks API v1
*   `tasklists().list()`: Abrufen aller Listen.
*   `tasks().list(tasklist=ID)`: Abrufen aller Tasks einer Liste.

#### Fitness API v1
*   `users().dataset().aggregate(...)`: Aggregieren von Datenpunkten (z.B. Schritte) über einen Zeitraum.
