# -*- coding: utf-8 -*-
"""
Fetch T212 Data - Enterprise Edition
Author: Gemini
Date: 2026-01-18
Version: 2.0.0

Changes:
- Async/Threaded Fetching for Performance
- Robust Error Handling & Logging
- Strict Typing
- Comprehensive Ticker Mapping
"""

import requests
import datetime
import os
import base64
import json
import time
import logging
import concurrent.futures
from typing import Dict, List, Optional, Any, Tuple
import yfinance as yf
import pandas as pd

# --- KONFIGURATION & LOGGING ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

API_KEY = "35211271ZsmeVZHQQODoFZSbqBqCRreRDsJsN"
API_SECRET = "aRJqiON-t61xEkN13xWlP5MsqYr02qBpKiUheCWRmFk"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR) # 14_TRADING
DASHBOARD_FILE = os.path.join(BASE_DIR, "04_DASHBOARDS", "T212_Dashboard.md")
DIVIDEND_FILE = os.path.join(BASE_DIR, "04_DASHBOARDS", "T212_Dividends.md")
CACHE_FILE = os.path.join(BASE_DIR, "02_DATA", "instruments_cache.json")
APP_JSON_FILE = os.path.join(BASE_DIR, "02_DATA", "portfolio_snapshot.json")

BASE_URL = "https://live.trading212.com/api/v0"
HEADERS = {"Authorization": f"Basic {base64.b64encode(f'{API_KEY}:{API_SECRET}'.encode()).decode()}"}

# --- ROBUST TICKER MAPPING ---
TICKER_OVERRIDES = {
    # DE / Xetra
    "SXR8d_EQ": "SXR8.DE",
    "VWCEd_EQ": "VWCE.DE",
    "IUSNd_EQ": "IUSN.DE",
    "EUNLd_EQ": "EUNL.DE",
    "BMWd_EQ": "BMW.DE",
    "VOW3d_EQ": "VOW3.DE",
    "SAPd_EQ": "SAP.DE",
    "RHMd_EQ": "RHM.DE",
    "DPWd_EQ": "DHL.DE",  # Rebranded to DHL
    "NTOd_EQ": "NTO.F",   # Frankfurt often better for japanese stocks in DE
    "KHEd_EQ": "KWH.F",   # Kawasaki Heavy Frankfurt
    "BAYNd_EQ": "BAYN.DE",
    
    # US / International Updates
    "SNE_US_EQ": "SONY",  # Sony Rebrand
    "DOW1_US_EQ": "DOW",  # Dow Inc
    "FB_US_EQ": "META",   # Meta Rebrand
    "OGZPY_US_EQ": "OGZPY",
    
    # UK / LSE (Suffix .L)
    "IITU_EQ": "IITU.L",
    "RRl_EQ": "RR.L",
    "BPl_EQ": "BP.L",
    "BAl_EQ": "BA.L",
    "LGENl_EQ": "LGEN.L",
    "VUSAl_EQ": "VUSA.L",
    
    # Amsterdam / Spain
    "SHELLa_EQ": "SHELL.AS",
    "REPe_EQ": "REP.MC",
    "LOGe_EQ": "LOG.MC"
}

def convert_to_yahoo_ticker(t212_ticker: str) -> str:
    """Converts Trading 212 internal tickers to Yahoo Finance tickers."""
    if t212_ticker in TICKER_OVERRIDES:
        return TICKER_OVERRIDES[t212_ticker]

    # Pattern Matching Heuristics
    ticker = t212_ticker
    if "_US_EQ" in ticker: ticker = ticker.replace("_US_EQ", "")
    elif "d_EQ" in ticker: ticker = ticker.replace("d_EQ", ".DE")
    elif "l_EQ" in ticker: ticker = ticker.replace("l_EQ", ".L")
    elif "a_EQ" in ticker: ticker = ticker.replace("a_EQ", ".AS")
    elif "e_EQ" in ticker: ticker = ticker.replace("e_EQ", ".MC")
    elif "x_EQ" in ticker: ticker = ticker.replace("x_EQ", ".DE")
    
    return ticker

# --- CACHE MANAGEMENT ---
def load_cache() -> Dict:
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.warning(f"Cache corrupted, starting fresh: {e}")
    return {}

def save_cache(data: Dict):
    try:
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        logger.error(f"Could not save cache: {e}")

# --- DATA FETCHING (CORE) ---
def get_t212_data() -> Tuple[Dict, List, Dict, List]:
    """Fetches base data from Trading 212 API."""
    try:
        with requests.Session() as s:
            s.headers.update(HEADERS)
            
            cash = s.get(f"{BASE_URL}/equity/account/cash").json()
            positions = s.get(f"{BASE_URL}/equity/portfolio").json()
            dividends = s.get(f"{BASE_URL}/equity/history/dividends").json().get("items", [])
            
            # Use cached metadata or empty dict
            ticker_map = load_cache()
            
            return cash, positions, ticker_map, dividends
    except Exception as e:
        logger.error(f"T212 API Error: {e}")
        return {}, [], {}, []

def fetch_yahoo_details(ticker: str, yf_ticker: str) -> Dict[str, Any]:
    """Worker function to fetch single ticker details."""
    result = {"ticker": ticker, "success": False, "data": {}}
    try:
        t = yf.Ticker(yf_ticker)
        
        # 1. Info (Metadata)
        info = t.info
        result["data"]["sector"] = info.get("sector", "Unbekannt")
        result["data"]["country"] = info.get("country", "Unbekannt")
        result["data"]["name"] = info.get("shortName") or info.get("longName") or ticker
        result["data"]["payout_ratio"] = info.get("payoutRatio", 0) or 0
        
        # 2. Dividends (History -> CAGR)
        divs = t.dividends
        cagr = 0.0
        if divs is not None and not divs.empty:
            yearly = divs.resample('YE').sum()
            current_year = datetime.datetime.now().year
            full_years = yearly[yearly.index.year < current_year]
            
            if len(full_years) >= 6:
                end_val = full_years.iloc[-1]
                start_val = full_years.iloc[-6]
                if start_val > 0 and end_val > 0:
                    cagr = (end_val / start_val)**(1/5) - 1
        
        result["data"]["div_cagr_5y"] = cagr
        
        # 3. Next Dividend (Estimation)
        est_date = None
        est_amt = 0.0
        
        if divs is not None and not divs.empty:
            last_pay = divs.sort_index().tail(1)
            if not last_pay.empty:
                last_date = last_pay.index[0]
                days_since = (datetime.datetime.now() - last_date).days
                freq = 91 if days_since < 120 else 365 # Simple Heuristic
                
                next_date = last_date + datetime.timedelta(days=freq)
                while next_date < datetime.datetime.now():
                    next_date += datetime.timedelta(days=freq)
                
                est_date = next_date
                est_amt = last_pay.iloc[0]

        result["data"]["next_pay_date"] = est_date
        result["data"]["next_pay_amount"] = est_amt
        result["success"] = True
        
    except Exception as e:
        # Silent fail for individual tickers is preferred to avoid spam
        # logger.debug(f"Failed to fetch {yf_ticker}: {e}")
        pass
        
    return result

def enrich_data_parallel(positions: List, ticker_map: Dict) -> Tuple[Dict, List]:
    """Enriches data using ThreadPoolExecutor for speed."""
    print("🚀 Starte parallele Analyse (Yahoo Finance)...")
    
    tasks = []
    future_divs = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for p in positions:
            ticker = p.get('ticker')
            
            # Skip if we have FRESH data (cache strategy could be improved, but for now we re-check div dates)
            # Actually, to get 'next_pay_date' accurate, we should check often. 
            # We will always check, but with threads it's fast.
            
            yf_sym = convert_to_yahoo_ticker(ticker)
            tasks.append(executor.submit(fetch_yahoo_details, ticker, yf_sym))
            
        # Collect results
        for future in concurrent.futures.as_completed(tasks):
            res = future.result()
            t = res["ticker"]
            
            if res["success"]:
                # Update Map
                if t not in ticker_map: ticker_map[t] = {}
                ticker_map[t].update(res["data"])
                
                # Extract Future Divs
                d_date = res["data"].get("next_pay_date")
                d_amt = res["data"].get("next_pay_amount", 0)
                
                if d_date and d_amt > 0:
                    qty = next((x['quantity'] for x in positions if x['ticker'] == t), 0)
                    future_divs.append({
                        "ticker": t,
                        "pay_date": d_date,
                        "amount_per_share": d_amt,
                        "quantity": qty
                    })
    
    # Clean up non-serializable objects for JSON cache
    # Dates in cache need to be strings? No, cache logic handles dicts.
    # But for 'save_cache', we should probably keep it simple.
    # We strip datetime objects from ticker_map before saving, or store them as strings.
    # For now, we only save the static metadata in cache, not the volatile 'next_pay_date'.
    
    cache_to_save = {}
    for k, v in ticker_map.items():
        cache_to_save[k] = {
            "name": v.get("name"),
            "sector": v.get("sector"),
            "country": v.get("country"),
            "payout_ratio": v.get("payout_ratio"),
            "div_cagr_5y": v.get("div_cagr_5y")
        }
    
    save_cache(cache_to_save)
    return ticker_map, future_divs

# --- MARKDOWN GENERATION ---
def create_dashboard(cash, positions, ticker_map) -> str:
    total = cash.get('total', 0)
    free = cash.get('free', 0)
    invested = cash.get('invested', 0)
    ppl = cash.get('ppl', 0)
    
    perf_pct = (ppl / invested * 100) if invested > 0 else 0
    icon = "🟢" if ppl >= 0 else "🔴"
    now = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    
    pos_sorted = sorted(positions, key=lambda x: (x.get('quantity', 0) * x.get('currentPrice', 0)), reverse=True)
    
    # Allocations
    sectors = {}
    countries = {}
    for p in positions:
        t = p['ticker']
        val = p['quantity'] * p['currentPrice']
        meta = ticker_map.get(t, {})
        s = meta.get("sector", "Unbekannt")
        c = meta.get("country", "Unbekannt")
        sectors[s] = sectors.get(s, 0) + val
        countries[c] = countries.get(c, 0) + val
        
    md = f"# 🦅 Trading Cockpit\n> **Update:** {now}\n\n"
    md += f"## 💰 Finanz-Übersicht\n| Metrik | Wert |\n| :--- | :--- |\n"
    md += f"| **Gesamtwert** | **{total:,.2f} €** |\n| 💸 Investiert | {invested:,.2f} € |\n| 💵 Cash | {free:,.2f} € |\n"
    md += f"| 📈 G/V | {icon} {ppl:,.2f} € ({perf_pct:.2f}%) |\n\n"
    md += "> **Qualität:** 💎=Top (CAGR>5%, Payout<80%) | 🚀=Growth (>10%) | ⚠️=Payout>100% | 🔻=Kürzung\n\n---\n\n"
    
    # Charts
    md += "## 🍰 Portfolio Allokation\n### Top 10 Holdings\n```mermaid\npie title Nach Wert\n"
    for p in pos_sorted[:10]:
        n = ticker_map.get(p['ticker'], {}).get("name", p['ticker']).replace('"', '').replace("'", "")[:15]
        v = p['quantity'] * p['currentPrice']
        md += f'    "{n}" : {v:.0f}\n'
    md += "```\n\n### Sektoren\n```mermaid\npie title Nach Sektor\n"
    for k, v in sorted(sectors.items(), key=lambda x: x[1], reverse=True)[:10]:
        clean_k = k.replace('"', '')
        md += f'    "{clean_k}" : {v:.0f}\n'
    md += "```\n\n"
    
    # Table
    md += "## 📊 Positionen\n| Name | Sektor | Wert | G/V | Quali |\n| :--- | :--- | :--- | :--- | :--- |\n"
    for p in pos_sorted:
        t = p['ticker']
        meta = ticker_map.get(t, {})
        val = p['quantity'] * p['currentPrice']
        pl_pct = (p.get('ppl',0) / (p['quantity']*p['averagePrice']) * 100) if p['averagePrice'] > 0 else 0
        
        cagr = meta.get("div_cagr_5y", 0) * 100
        payout = meta.get("payout_ratio", 0) * 100
        q_icon = ""
        if payout > 100: q_icon = "⚠️"
        elif cagr < 0: q_icon = "🔻"
        elif cagr > 10: q_icon = "🚀"
        elif cagr > 5 and payout < 80: q_icon = "💎"
        
        name = meta.get("name", t)
        md += f"| **{name}** | {meta.get('sector','-')} | {val:,.2f} € | {pl_pct:.2f}% | {q_icon} |\n"
        
    return md

def create_dividend_md(dividends, ticker_map, positions, future_divs) -> str:
    now = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    md = f"# 📅 Dividenden-Kalender\n> **Update:** {now}\n\n"
    
    # Quality Table
    md += "## 💎 Quality Check\n| Unternehmen | CAGR 5Y | Payout | Status |\n| :--- | :--- | :--- | :--- |\n"
    sorted_pos = sorted(positions, key=lambda x: ticker_map.get(x['ticker'], {}).get('div_cagr_5y', 0), reverse=True)
    for p in sorted_pos:
        t = p['ticker']
        meta = ticker_map.get(t, {})
        cagr = meta.get("div_cagr_5y", 0)
        if cagr == 0: continue
        payout = meta.get("payout_ratio", 0)
        
        status = "✅"
        if payout > 1.0: status = "⚠️"
        if cagr < 0: status = "🔻"
        if cagr > 0.10: status = "🚀"
        if cagr > 0.05 and payout < 0.8: status = "💎"
        
        md += f"| **{meta.get('name', t)}** | {cagr*100:.2f}% | {payout*100:.2f}% | {status} |\n"
    
    # Forecast
    md += "\n## 🔮 Prognose\n"
    if future_divs:
        future_divs.sort(key=lambda x: x['pay_date'])
        grouped = {}
        for x in future_divs:
            k = (x['pay_date'].year, x['pay_date'].month)
            if k not in grouped: grouped[k] = []
            grouped[k].append(x)
            
        months = {1:"Jan", 2:"Feb", 3:"Mär", 4:"Apr", 5:"Mai", 6:"Jun", 7:"Jul", 8:"Aug", 9:"Sep", 10:"Okt", 11:"Nov", 12:"Dez"}
        
        for (y, m), items in sorted(grouped.items()):
            if (y, m) < (datetime.datetime.now().year, datetime.datetime.now().month): continue
            md += f"### {months.get(m)} {y}\n| Tag | Unternehmen | Betrag |\n| :--- | :--- | :--- |\n"
            total = 0
            for i in items:
                v = i['quantity'] * i['amount_per_share']
                total += v
                n = ticker_map.get(i['ticker'], {}).get("name", i['ticker'])
                md += f"| {i['pay_date'].day}. | {n} | {v:,.2f} € |\n"
            md += f"| **Summe** | | **~{total:,.2f} €** |\n\n"
    else:
        md += "Keine Prognosedaten verfügbar.\n"
        
    return md

# --- MAIN ---
if __name__ == "__main__":
    print("🚀 Starting T212 Sync (Enterprise v2.0)...")
    
    # 1. Fetch Basic
    cash, positions, ticker_map, dividends = get_t212_data()
    
    if positions:
        # 2. Parallel Enrich
        ticker_map, future_divs = enrich_data_parallel(positions, ticker_map)
        
        # 3. Write Markdown
        with open(DASHBOARD_FILE, "w", encoding="utf-8") as f:
            f.write(create_dashboard(cash, positions, ticker_map))
            
        with open(DIVIDEND_FILE, "w", encoding="utf-8") as f:
            f.write(create_dividend_md(dividends, ticker_map, positions, future_divs))
            
        # 4. JSON Dump for App (Strict Format)
        app_data = {
            "cash": cash,
            "positions": positions,
            "metadata": ticker_map,
            # Serialize dates for JSON
            "future_divs": [
                {
                    "ticker": x["ticker"],
                    "pay_date": x["pay_date"].isoformat() if x["pay_date"] else None,
                    "amount": x["amount_per_share"],
                    "qty": x["quantity"]
                } for x in future_divs
            ]
        }
        with open(APP_JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(app_data, f, indent=2)
            
        print("✅ Data Sync Complete.")
    else:
        print("❌ Failed to fetch T212 data.")