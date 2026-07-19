import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

message = """🚀 إشارة تجريبية

العملة: BTCUSDT
النوع: LONG
الدخول: 100000
الهدف: 101000
وقف الخسارة: 99500
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})

print("Signal sent!")
