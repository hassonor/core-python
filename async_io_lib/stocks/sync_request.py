import time

import requests
import os

api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = [
    "AAPL", "MSFT", "AMZN", "GOOG", "GOOGL", "FB", "TSLA", "BRK.A", "BRK.B", "V",
    "JNJ", "WMT", "PG", "MA", "DIS", "NVDA", "HD", "PYPL", "BAC", "VZ",
    "ADBE", "CMCSA", "NFLX", "KO", "NKE", "MRK", "PEP", "T", "PFE", "INTC",
    "CRM", "ABT", "ORCL", "ABBV", "CSCO", "TMO", "ACN", "AVGO", "XOM", "COST",
    "CVX", "LMT", "DHR", "MDT", "NEE", "BMY", "UNH", "AMGN", "MCD", "WFC",
    "TXN", "QCOM", "HON", "LIN", "BA", "UNP", "SBUX", "IBM", "RTX", "MMM",
    "UPS", "CAT", "GE", "GS", "C", "JPM", "VZ", "CVS", "DOW", "INTU"
]
results = []

start = time.time()
for symbol in symbols:
    response = requests.get(url.format(symbol, api_key))
    results.append(response.json())
end = time.time()
total_time = end - start
print(f"It took {total_time} seconds to make {len(symbols)} API calls")
print('You did it!')
