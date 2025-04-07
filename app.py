# app.py
from flask import Flask, jsonify
from scraper import scrape_option_chain

app = Flask(__name__)

@app.route("/")
def home():
    return "NSE Option Chain Scraper API"

@app.route('/scrape-now', methods=['GET'])
def scrape_now():
    try:
        scrape_option_chain(symbol="NIFTY") 
        scrape_option_chain(symbol="BANKNIFTY") 
        scrape_option_chain(symbol="FINNIFTY")
        scrape_option_chain(symbol="NIFTYMID50")
        scrape_option_chain(symbol="MIDCPNIFTY")
        return jsonify({'status': 'success', 'message': 'Scraping done!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
