import requests

def analyze_btc():
    url = "https://fapi.binance.com/fapi/v1/ping"

    response = requests.get(url, timeout=10)

    return {
        "signal": "🟢 LONG",
        "price": response.status_code,
        "ema": "OK"
    }
