# scraper.py
import requests
import json
from datetime import datetime

def scrape_option_chain(symbol="NIFTY"):
    url = f"https://www.nseindia.com/api/option-chain-indices?symbol={symbol}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US,en;q=0.9",
    }

    session = requests.Session()
    session.headers.update(headers)
    try:
        response = session.get(url, timeout=10)
        data = response.json()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = f"option_chain_{symbol}_{now.replace(':', '-')}.json"
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        return data
    except Exception as e:
        return {"error": str(e)}
