import requests
import pandas as pd
from datetime import datetime
import os

def scrape_option_chain(symbol="NIFTY"):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    url = f"https://www.nseindia.com/api/option-chain-indices?symbol={symbol}"
    session = requests.Session()
    session.headers.update(headers)
    session.get("https://www.nseindia.com/option-chain")

    try:
        response = session.get(url, timeout=10)
        data = response.json()

        records = []
        for item in data['records']['data']:
            strike_price = item.get("strikePrice", "")
            expiry_date = item.get("expiryDate", "")
            ce = item.get("CE", {})
            pe = item.get("PE", {})

            record = {
                "strikePrice": strike_price,
                "expiryDate": expiry_date,
                "CE_openInterest": ce.get("openInterest", None),
                "CE_changeInOI": ce.get("changeinOpenInterest", None),
                "CE_volume": ce.get("totalTradedVolume", None),
                "CE_iv": ce.get("impliedVolatility", None),
                "CE_ltp": ce.get("lastPrice", None),
                "PE_openInterest": pe.get("openInterest", None),
                "PE_changeInOI": pe.get("changeinOpenInterest", None),
                "PE_volume": pe.get("totalTradedVolume", None),
                "PE_iv": pe.get("impliedVolatility", None),
                "PE_ltp": pe.get("lastPrice", None),
            }

            records.append(record)

        df = pd.DataFrame(records)
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        os.makedirs("data", exist_ok=True)
        filename = f"data/option_chain_{symbol}_{now}.csv"
        df.to_csv(filename, index=False)

        return {
            "status": "success",
            "rows": len(df),
            "filename": filename
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}
