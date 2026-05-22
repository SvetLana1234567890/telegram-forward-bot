from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = 8689968489:AAFr9p2oQuFo3e79JinPdk7FTAvspwUQL5E
TARGET_CHAT_ID = -1005103853856


async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message:
        return

    # Не пересилати повідомлення з цільової групи
    if update.effective_chat.id == TARGET_CHAT_ID:
        return

    source_chat = update.effective_chat.title
    text = update.message.text or ""

    message = f"🏪 Магазин: {source_chat}\n\n{text}"

    await context.bot.send_message(
        chat_id=TARGET_CHAT_ID,
        text=message
    )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message)
)

print("Bot started...")

app.run_polling()
