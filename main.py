from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from handlers.register import register, handle_class
from config import TOKEN
from database.db import init_db
from telegram.ext import MessageHandler, filters, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌑 Welcome to Night Lord V2"
    )


def main():
    init_db()

    app.add_handler(CommandHandler(["register", "ثبت_نام"], register))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_class))
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Night Lord V2 Started")

    app.run_polling()


if __name__ == "__main__":
    main()
