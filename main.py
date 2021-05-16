import pandas as pd
from flask import Flask, render_template, url_for
import requests
import os
from datetime import datetime
from configparser import ConfigParser

app = Flask(__name__)

config = ConfigParser()
config.read('params.ini')

# Get variables from params.ini file.
# Fallback variables for Bitcoin provided if variables not available in params.ini file.
SYMBOL = config.get("main", "SYMBOL", fallback="BTC")
NAME = config.get("main", "NAME", fallback="Bitcoin")
MARKET = config.get("main", "MARKET", fallback="GBP")
FUNCTION = config.get("main", "FUNCTION", fallback="DIGITAL_CURRENCY_DAILY")

CRYPTO_ENDPOINT = "https://www.alphavantage.co/query"
API_KEY = os.environ.get("api_key")  # Accessed from environment variables

crypto_parameters = {
    "function": FUNCTION,
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

    # current date and time
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")

    try:
        # Converts to pandas dataframe and remove metadata
        crypto_df = pd.DataFrame(crypto_data["Time Series (Digital Currency Daily)"], index=None)

        # Change row names for the display
        crypto_df.index = ["Open (GBP)", "Open (USD)", "High (GBP)", "High (USD)", "Low (GBP)", "Low (USD)",
                           "Close (GBP)", "Close (USD)", "Volume", "Market cap (USD)"]

        # Extract data for current date
        crypto_endpoint = (crypto_df[f"{date}"])
        image_file = url_for('static', filename="images/cryptocurrency.png")
        return render_template("index.html", data=crypto_endpoint, name=NAME, image=image_file, date=date)

    except KeyError:
        return render_template("error.html")


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
