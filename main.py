import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, filters, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("Bot aktif! /ders yaz")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
