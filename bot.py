from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = "8689968489:AAFr9p2oQuFo3e79JinPdk7FTAvspwUQL5E"
TARGET_CHAT_ID = -5103853856


async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = update.effective_message

    if not message:
        return

    text = message.text or message.caption

    if not text:
        return

    await context.bot.send_message(
        chat_id=TARGET_CHAT_ID,
        text=f"🏪 {update.effective_chat.title}\n\n{text}"
    )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.ALL, forward_message)
)

print("Bot started...")

app.run_polling()

