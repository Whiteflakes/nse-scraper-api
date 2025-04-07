# app.py
from flask import Flask, jsonify
from scraper import scrape_option_chain

app = Flask(__name__)

@app.route("/")
def home():
    return "NSE Option Chain Scraper API"

@app.route("/scrape")
def scrape():
    data = scrape_option_chain()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
