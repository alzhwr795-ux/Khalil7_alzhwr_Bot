print("Starting bot...")
from analysis import analyze_btc

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

try:
    result = analyze_btc()

    message = f"""
🚀 توصية تجريبية

العملة: BTCUSDT

النوع: {result['signal']}

السعر الحالي: {result['price']}

EMA20: {result['ema']}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

    print("Signal sent successfully!")

except Exception as e:
    print("ERROR:", e)
    raise
