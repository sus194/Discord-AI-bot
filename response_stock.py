import os
import requests

def get_stock_price(symbol):
    API_KEY = os.environ['STOCK_API_KEY']
    symbol = symbol.upper()
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    price = data.get("Global Quote").get("05. price")
    print(price)
    return price