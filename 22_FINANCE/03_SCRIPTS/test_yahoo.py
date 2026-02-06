import requests
import json
import datetime

# Test-Ticker: Realty Income (O) und Apple (AAPL)
tickers = ["O", "AAPL"]
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

print("Testing Yahoo Finance Access...")

for symbol in tickers:
    try:
        url = f"https://query2.finance.yahoo.com/v10/finance/quoteSummary/{symbol}?modules=calendarEvents,summaryDetail"
        r = requests.get(url, headers=headers, timeout=5)
        
        if r.status_code == 200:
            data = r.json()
            cal = data.get("quoteSummary", {}).get("result", [])[0].get("calendarEvents", {})
            
            print(f"\n--- {symbol} ---")
            if 'exDividendDate' in cal:
                print(f"Ex-Date: {cal['exDividendDate'].get('fmt')}")
            if 'dividendDate' in cal:
                print(f"Pay-Date: {cal['dividendDate'].get('fmt')}")
            
            # Dividendenrate
            summary = data.get("quoteSummary", {}).get("result", [])[0].get("summaryDetail", {})
            print(f"Rate: {summary.get('dividendRate', {}).get('fmt')} (Yield: {summary.get('dividendYield', {}).get('fmt')})")
        else:
            print(f"Error for {symbol}: {r.status_code}")
            
    except Exception as e:
        print(f"Exception for {symbol}: {e}")
