from flask import Flask
import threading, os
import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Flask - Render Live olması için
flask_app = Flask(__name__)
@flask_app.route('/')
def home(): return "Bot calisiyor!"

def run_flask():
    flask_app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

threading.Thread(target=run_flask, daemon=True).start()

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("Bot aktif! /ders yaz")

async def dersler(update, context):
    await update.message.reply_text("KPSS Notlarin hazir! n-Tarih: Osmanli Kurulusu...")

async def mesaj_isle(update, context):
    metin = update.message.text
    await update.message.reply_text(f"Aldim: {metin} - Bunun üzerine çalışalım!")

def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ders", dersler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mesaj_isle))
    print("Bot başlatılıyor...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
