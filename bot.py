from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = "8689968489:AAFr9p2oQuFo3e79JinPdk7FTAvspwUQL5E"
TARGET_CHAT_ID = -5103853856


async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = update.effective_message

    if not message:
        return

    source = update.effective_chat.title or "Unknown"

    # 🔥 універсальний витяг тексту
    text = (
        message.text
        or message.caption
        or (message.to_dict().get("text"))
        or ""
    )

    # ❗ якщо це бот-замовлення без text взагалі
    if not text:
        text = str(message)

    await context.bot.send_message(
        chat_id=TARGET_CHAT_ID,
        text=f"🏪 {source}\n\n{text}"
    )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.ALL, forward_message))
app.add_handler(ChannelPostHandler(forward_message))

print("Bot started...")

app.run_polling()

