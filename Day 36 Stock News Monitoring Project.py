import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "CI0BFTH8T9NNO6NZ"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_params = {
    'functions': "TIME_SERIES_DAILY",
    'symbol': "STOCK_NAME",
    'api_key': "STOCK_API_KEY",
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
print(response.json())


