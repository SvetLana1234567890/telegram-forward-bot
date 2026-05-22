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

    message = update.effective_message

    if not message:
        return

    text = message.text or message.caption or str(message.to_dict())

    await context.bot.send_message(
        chat_id=TARGET_CHAT_ID,
        text=text
    )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.ALL, forward_message))

print("Bot started...")

app.run_polling()
