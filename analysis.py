import requests

def analyze_btc():
    url = "https://api.bybit.com/v5/market/tickers?category=linear&symbol=BTCUSDT"

    response = requests.get(url, timeout=10)
    data = response.json()

    price = float(data["result"]["list"][0]["lastPrice"])

    signal = "🟢 LONG"

    return {
        "signal": signal,
        "price": price,
        "ema": "قيد التطوير"
    }
