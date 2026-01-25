import unittest
import json
import os
import sys

# Add parent dir to path to import scripts if needed, 
# but here we mostly test the data structure validity for the app.

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR) # parent of tests/ is 14_TRADING
PORTFOLIO_FILE = os.path.join(BASE_DIR, "02_DATA", "portfolio_snapshot.json")
BANKING_FILE = os.path.join(BASE_DIR, "02_DATA", "banking_snapshot.json")

class TestFinanceData(unittest.TestCase):
    
    def test_files_exist(self):
        """Prüft, ob die kritischen Datendateien existieren."""
        self.assertTrue(os.path.exists(PORTFOLIO_FILE), "Portfolio JSON fehlt")
        self.assertTrue(os.path.exists(BANKING_FILE), "Banking JSON fehlt")

    def test_portfolio_json_structure(self):
        """Prüft das Schema der Portfolio-Datei."""
        with open(PORTFOLIO_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        self.assertIn("cash", data)
        self.assertIn("positions", data)
        self.assertIsInstance(data["positions"], list)
        
        # Check Values
        cash = data.get("cash", {})
        self.assertIsInstance(cash.get("total", 0), (int, float))

    def test_banking_json_structure(self):
        """Prüft das Schema der Banking-Datei."""
        with open(BANKING_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        self.assertIn("sparkasse_balance", data)
        self.assertIn("revolut_balance", data)
        self.assertIsInstance(data.get("net_worth_history", []), list)

    def test_calculation_integrity(self):
        """Prüft, ob Net Worth logisch berechnet werden kann."""
        with open(PORTFOLIO_FILE, "r", encoding="utf-8") as f: p = json.load(f)
        with open(BANKING_FILE, "r", encoding="utf-8") as f: b = json.load(f)
        
        t212 = p.get("cash", {}).get("total", 0)
        bank = b.get("sparkasse_balance", 0) + b.get("revolut_balance", 0)
        net_worth = t212 + bank
        
        self.assertGreater(net_worth, 0, "Net Worth sollte positiv sein (hoffentlich!)")

if __name__ == '__main__':
    unittest.main()
