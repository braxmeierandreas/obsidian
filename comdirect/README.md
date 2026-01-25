# comdirect REST API Integration

Dieses Verzeichnis enthält Dokumentation und Konfiguration für die comdirect REST API.
Die eigentlichen Skripte befinden sich in `00_SCRIPTS/`.

## 🚀 Einrichtung

1. **API-Zugang:** Erstelle eine App im [comdirect Developer Portal](https://api-developer.comdirect.de/).
2. **Setup-Skript:** Führe das Setup-Skript aus, um deine Credentials sicher zu speichern:
   ```powershell
   python 00_SCRIPTS/comdirect_setup.py
   ```
3. **Synchronisierung:** Starte die Synchronisierung deiner Kontostände:
   ```powershell
   python 00_SCRIPTS/bank_sync_comdirect.py
   ```

## 📂 Enthaltene Dateien (Original)
- `comdirect_REST_API_Dokumentation.pdf`: Offizielle API-Dokumentation.
- `Python-Quelldatei (neu).json`: OpenAPI/Swagger-Spezifikation.
- `Python-Quelldatei (neu) (2).json`: Postman Collection für Tests.

## 🛠️ Funktionsweise
Das Skript `bank_sync_comdirect.py` nutzt den **OAuth2 Resource Owner Password Credentials Flow**.
- Bei der ersten Ausführung (oder nach Session-Ablauf) ist eine **PhotoTAN** erforderlich.
- Die Challenge wird als `00_SCRIPTS/comdirect_challenge.png` gespeichert und muss gescannt werden.
- Die Kontostände werden in `14_TRADING/02_DATA/banking_snapshot.json` gespeichert und fließen in das Dashboard ein.
