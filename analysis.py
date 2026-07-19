import requests

def analyze_btc():
    url = "https://api.binance.com/api/v3/ping"

    response = requests.get(url, timeout=10)

    return {
        "signal": "🟢 LONG",
        "price": response.status_code,
        "ema": "OK"
    }
