import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

async def baslangic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Merhaba! Ders Asistanı Bot aktif kanka ✅ /ders yaz")

async def dersler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("KPSS Notların hazır:\n- Tarih: Osmanlı Kuruluşu\n- Vatandaşlık yakında...")

async def mesaj_isle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    metin = update.message.text
    await update.message.reply_text(f"Aldım:{metin} - Bunun üzerine çalışalım!")

def ana():
    uygulama = ApplicationBuilder().token(TOKEN).build()
    uygulama.add_handler(CommandHandler("start", baslangic))
    uygulama.add_handler(CommandHandler("ders", dersler))
    uygulama.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mesaj_isle))
    print("Botlar....")
    uygulama.run_polling()

if __name__ == "__main__":
    ana()
