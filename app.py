import requests
import json
from flask import Flask
from healthcheck import HealthCheck

app = Flask(__name__)
health = HealthCheck()

## Function definition for fetching spot price from coinbase api
def get_spot_price(currency):
    url = "https://api.coinbase.com/v2/prices/spot?currency={}".format(currency)
    response = requests.get(url)
    if response.status_code == 200:
        try:
            price = response.json()
            return price
        except(KeyError, IndexError) as e:
            # print(e)
            return e
    else:
        print("Respons: ", type(response))
        return response

## Adding health endpoint using healthcheck() function
app.add_url_rule("/health","health",view_func=lambda: health.run())

## Route for root
@app.route("/")
def index():
    return "Welcome"

## Takes currency as variable and calls the get price function for that currency
@app.route("/<curr>")
def price_in_curr(curr):
    spot_price = get_spot_price(curr)
    return spot_price

## Endpoint for Healthcheck
# @app.route("/health")
# def health():
#     return { 'success': True, 'message': "healthy" }

# ## Returns BTC Spot price in USD
# @app.route("/USD")
# def price_in_usd():
#     price_usd = get_spot_price("USD")
#     return price_usd

if __name__ == '__main__':
    app.run(port=8080,host="0.0.0.0",debug=True)