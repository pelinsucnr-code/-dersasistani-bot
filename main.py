import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Merhaba! Ders Asistanı Bot aktif kanka ✅\n/ders yaz yeter.")

async def ders(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("KPSS Notların hazır:\n- Tarih: Osmanlı kuruluş\n- Matematik: 10 soru\nNe çalışmak istersin?")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"Aldım: {text} - Bunun üzerine çalışalım!")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ders", ders))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot çalışıyor...")
    app.run_polling()

if __name__ == "__main__":
    main()
