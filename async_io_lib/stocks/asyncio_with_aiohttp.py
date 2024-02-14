import time
import asyncio
import aiohttp
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


def get_tasks(session):
    tasks = []
    for symbol in symbols:
        tasks.append(asyncio.create_task(session.get(url.format(symbol, api_key), ssl=False)))
    return tasks


async def get_symbols():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await response.json())


asyncio.run(get_symbols())

# The same as:
# loop = asyncio.get_event_loop()
# loop.run_until_complete(get_symbols())
# loop.close()

end = time.time()
total_time = end - start
print(f"It took {total_time} seconds to make {len(symbols)} API calls")
print('You did it!')
