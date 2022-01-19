import requests
import json
from flask import Flask
from healthcheck import HealthCheck
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
health = HealthCheck()
metrics = PrometheusMetrics(app)

metrics.info('app_info', 'Application info', version='1.0.3')

## Function definition for fetching spot price from coinbase api
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
        # print("Respons: ", type(response))
        return None

## Adding health endpoint using healthcheck() function
app.add_url_rule("/health","health",view_func=lambda: health.run())

## Route for root
@app.route("/")
def index():
    return "Welcome to ZeroHash"

## Takes currency as variable and calls the get price function for that currency
@app.route("/<curr>")
def price_in_curr(curr):
    spot_price = get_spot_price(curr)
    return spot_price

## Endpoint for Health check with simple json response
# @app.route("/health")
# def health():
#     return { 'success': True, 'message': "healthy" }

## Returns Spot price in currency passed as parameter
# @app.route("/USD")
# def price_in_usd():
#     price_usd = get_spot_price("USD")
#     return price_usd

# @app.route("/EUR")
# def price_in_eur():
#     price_eur = get_spot_price("EUR")
#     return price_eur

# @app.route("/GBP")
# def price_in_gbp():
#     price_gbp = get_spot_price("GBP")
#     return price_gbp

# @app.route("/JPY")
# def price_in_jpy():
#     price_jpy = get_spot_price("JPY")
#     return price_jpy

# @app.route("/inr")
# def price_in_inr():
#     price_inr = get_spot_price("inr")
#     return price_inr

if __name__ == '__main__':
    app.run(port=8080,host="0.0.0.0",debug=True)