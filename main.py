from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from config import TOKEN
from database.db import init_db


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌑 Welcome to Night Lord V2"
    )


def main():
    init_db()

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Night Lord V2 Started")

    app.run_polling()


if __name__ == "__main__":
    main()
