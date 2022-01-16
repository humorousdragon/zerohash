import requests
import json
import sys
from flask import Flask
from datetime import datetime as dt
import os
# from healthcheck import HealthCheck

# EUR, GBP, USD and JPY
app = Flask(__name__)
# health = HealthCheck(app, '/health')

def get_spot_price(currency):
    url = "https://api.coinbase.com/v2/prices/spot?currency={}".format(currency)
    response = requests.get(url)
    if response.status_code == 200:
        try:
            price = response.json()
            return price
        except(KeyError, IndexError) as e:
            print(e)
            return None
    else:
        return None

@app.route("/")
def index():
    return "Welcome"

@app.route("/<curr>")
def price_in_curr(curr):
    spot_price = get_spot_price(curr)
    return spot_price

@app.route("/health")
def health():
    return 200

## Returns BTC Spot price in USD
@app.route("/USD")
def price_in_usd():
    price_usd = get_spot_price("USD")
    return price_usd

if __name__ == '__main__':
    app.run(port=8080,host="0.0.0.0",debug=True)