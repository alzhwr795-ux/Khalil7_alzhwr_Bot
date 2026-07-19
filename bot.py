import os
import requests
from analysis import analyze_btc

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

result = analyze_btc()

message = f"""🚀 تحليل تجريبي

العملة: BTCUSDT

النوع: {result['signal']}

السعر الحالي: {result['price']}

EMA: {result['ema']}
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})

print("Signal sent!")
