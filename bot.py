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

     print("\n========== RAW UPDATE ==========\n")
    print(update.to_dict())
    print("\n================================\n")

    msg = update.message or update.edited_message or update.channel_post

    if not msg:
        return

    text = getattr(msg, "text", None) or getattr(msg, "caption", None)

    if not text:
        text = str(msg)

    await context.bot.send_message(
        chat_id=TARGET_CHAT_ID,
        text=f"🏪 {update.effective_chat.title}\n\n{text}"
    )


async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await context.bot.send_message(
        chat_id=TARGET_CHAT_ID,
        text=f"🔘 Callback: {query.data}"
    )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.ALL, forward_message))

print("Bot started...")

app.run_polling()
