import requests

def analyze_btc():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

    response = requests.get(url, timeout=10)
    data = response.json()

    price = float(data["price"])

    if price > 100000:
        signal = "🟢 LONG"
    else:
        signal = "🔴 SHORT"

    return {
        "signal": signal,
        "price": price,
        "ema": "قيد الحساب"
    }
