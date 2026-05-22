from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes
)

TOKEN = "8689968489:AAFr9p2oQuFo3e79JinPdk7FTAvspwUQL5E"
TARGET_CHAT_ID = -5103853856


async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    msg = (
        update.message
        or update.edited_message
        or update.channel_post
    )

    if not msg:
        return

    text = msg.text or msg.caption or ""

    # fallback для forwarded bot messages
    if not text:
        text = str(msg.to_dict())

    await context.bot.send_message(
        chat_id=TARGET_CHAT_ID,
        text=f"🏪 {msg.chat.title}\n\n{text}"
    )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.ALL, forward_message))

print("Bot started...")

app.run_polling()
