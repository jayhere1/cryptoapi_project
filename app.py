import pandas as pd
from flask import Flask, render_template, send_file
import requests
import os
from datetime import datetime

app = Flask(__name__)

SYMBOL = "ETH"
NAME = "Ethereum"
MARKET = "GBP"

CRYPTO_ENDPOINT = "https://www.alphavantage.co/query"
API_KEY = os.environ.get("api_key")

crypto_parameters = {
    "function": "DIGITAL_CURRENCY_DAILY",  # returns the daily historical time series for a digital currency
    "symbol": SYMBOL,
    "market": MARKET,
    "apikey": API_KEY,
    "datatype": "json",
}


@app.route('/')
def home():
    crypto_response = requests.get(url=CRYPTO_ENDPOINT, params=crypto_parameters)
    crypto_response.raise_for_status()
    crypto_data = crypto_response.json()
    try:
        # Converts to pandas dataframe and remove metadata
        crypto_df = pd.DataFrame(crypto_data["Time Series (Digital Currency Daily)"], index=None)

        # current date and time
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")

        # Extract data for current date
        crypto_endpoint = (crypto_df[f"{date}"])
        return render_template("index.html", data=crypto_endpoint, symbol=SYMBOL, name=NAME)
    except KeyError:
        return render_template("error.html")


if __name__ == '__main__':
    app.run(debug=True)
