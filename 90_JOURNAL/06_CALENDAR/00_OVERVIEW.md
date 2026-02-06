# 📅 Calendar Control Center

Welcome to your personal calendar management system.

## 📂 Main Views
- **[[02_Tagebuch/04_Kalender/Kalender]]**: 
  - Your master timeline. Contains all events from your Google Calendars and local routines for the next 90 days.
  - *Updated automatically.*

## ⚙️ Configuration & Scripts
- **[[manage_calendar]]** (`.md` / `.py`): 
  - The "Engine". This script fetches your data and generates the calendar. 
  - *Note: Renamed to .md so you can read/edit it here, but executed as python.*

- **[[routines.json]]**: 
  - Define your recurring daily habits here (e.g., Morning Routine, Lunch).
  - *Keep this as .json.*

- **`update.bat`**: 
  - **👉 Click this file in Explorer to Refresh!**
  - Runs the script and updates [[02_Tagebuch/04_Kalender/Kalender]].

## 🚀 Quick Actions
1. **Edit Routines:** Open [[routines.json]] to change times or habits.
2. **Refresh:** Run `update.bat` to pull the latest events.
3. **View:** Open [[02_Tagebuch/04_Kalender/Kalender]] to see your schedule.
