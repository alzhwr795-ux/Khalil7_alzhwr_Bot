import ccxt

exchange = ccxt.binance()

def analyze_btc():
    ohlcv = exchange.fetch_ohlcv("BTC/USDT", timeframe="1h", limit=20)

    closes = [candle[4] for candle in ohlcv]

    ema20 = sum(closes) / len(closes)
    price = closes[-1]

    if price > ema20:
        signal = "🟢 LONG"
    else:
        signal = "🔴 SHORT"

    return {
        "signal": signal,
        "price": price,
        "ema": round(ema20, 2)
    }
