import os
import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("Bot aktif! /ders yaz")

async def dersler(update, context):
    await update.message.reply_text("KPSS Notların hazır! n-Tarih: Osmanlı Kuruluşu...")

async def mesaj_isle(update, context):
    metin = update.message.text
    await update.message.reply_text(f"Aldım: {metin} - Bunun üzerine çalışalım!")

def main():
    # Python 3.14 için event loop düzeltmesi
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ders", dersler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mesaj_isle))
    print("Botlar baslatiliyor...")
    app.run_polling()

if __name__ == "__main__":
    main()
