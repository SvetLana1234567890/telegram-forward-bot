from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = "8689968489:AAFr9p2oQuFo3e79JinPdk7FTAvspwUQL5E"
TARGET_CHAT_ID = "-5103853856"


async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = update.effective_message

    if not message:
        return

    source_chat = update.effective_chat.title

    text = (
        message.text
        or message.caption
        or ""
    )

    # якщо тексту немає — беремо JSON-опис
    if not text:
        text = str(message.to_dict())

    new_text = f"🏪 Магазин: {source_chat}\n\n{text}"

    await context.bot.send_message(
        chat_id=TARGET_CHAT_ID,
        text=new_text
    )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.ALL, forward_message)
)

print("Bot started...")

app.run_polling()
print("CHAT ID:", update.effective_chat.id)
