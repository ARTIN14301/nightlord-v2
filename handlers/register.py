from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

import sqlite3

DB = "nightlord.db"


def get_user(telegram_id):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE telegram_id=?", (telegram_id,))
    user = cur.fetchone()

    conn.close()
    return user


def create_user(telegram_id, username, first_name, user_class):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO users (telegram_id, username, first_name, class)
    VALUES (?, ?, ?, ?)
    """, (telegram_id, username, first_name, user_class))

    conn.commit()
    conn.close()


async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.effective_user.id)

    if user:
        await update.message.reply_text("❌ شما قبلاً ثبت نام کرده‌اید.")
        return

    keyboard = [
        ["⚔ Warrior", "🛡 Knight"],
        ["🏹 Ranger", "🗡 Assassin"]
    ]

    await update.message.reply_text(
        "⚔ کلاس خود را انتخاب کن:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

    context.user_data["registering"] = True


async def handle_class(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data.get("registering"):
        return

    text = update.message.text

    classes = ["⚔ Warrior", "🛡 Knight", "🏹 Ranger", "🗡 Assassin"]

    if text not in classes:
        await update.message.reply_text("❌ لطفاً یکی از کلاس‌ها را انتخاب کن.")
        return

    user = update.effective_user

    create_user(
        user.id,
        user.username,
        user.first_name,
        text
    )

    context.user_data["registering"] = False

    await update.message.reply_text(
        f"""🎉 ثبت نام با موفقیت انجام شد!

👤 Name: {user.first_name}
⚔ Class: {text}
💰 Gold: 100
🏆 Level: 1

🌑 Welcome to Night Lord"""
    )
