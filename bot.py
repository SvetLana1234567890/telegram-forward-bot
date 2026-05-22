from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, TypeHandler
import os

TOKEN = "8689968489:AAFr9p2oQuFo3e79JinPdk7FTAvspwUQL5E"
TARGET_CHAT_ID = -5103853856


async def forward_all(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # беремо будь-яке доступне повідомлення
    msg = (
        update.message
        or update.edited_message
        or update.channel_post
    )

    if not msg:
        return

    # текст / caption / fallback
    text = msg.text or msg.caption

    if not text:
        text = str(msg.to_dict())

    chat_title = getattr(msg.chat, "title", "Unknown")

    await context.bot.send_message(
        chat_id=TARGET_CHAT_ID,
        text=f"🏪 {chat_title}\n\n{text}"
    )


app = ApplicationBuilder().token(TOKEN).build()

# 🔥 ВАЖЛИВО: ловимо ВСІ update
app.add_handler(TypeHandler(Update, forward_all))

print("Bot started...")

app.run_polling()
