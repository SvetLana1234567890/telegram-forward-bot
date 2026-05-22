from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "8689968489:AAFr9p2oQuFo3e79JinPdk7FTAvspwUQL5E"
TARGET_CHAT_ID = -5103853856


def extract_message(msg):
    """
    Нормалізує ВСІ типи повідомлень, які реально приходять в Bot API
    """

    if not msg:
        return None

    # 1. звичайний текст
    if msg.text:
        return msg.text

    # 2. підписи (фото/док/тощо)
    if msg.caption:
        return msg.caption

    # 3. fallback (forwarded / bot messages / weird cases)
    data = msg.to_dict()

    # найчастіше POS тут залишає текст
    if "text" in data and data["text"]:
        return data["text"]

    if "caption" in data and data["caption"]:
        return data["caption"]

    return str(data)


async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    msg = update.effective_message

    if not msg:
        return

    text = extract_message(msg)

    # 🧠 фільтр: ігноруємо сміття
    if not text:
        return

    # (опціонально) фільтр тільки замовлень
    if "Замовлення" not in text and "Попередн" not in text:
        return

    chat_title = update.effective_chat.title or "Unknown"

    final_text = f"🏪 {chat_title}\n\n{text}"

    await context.bot.send_message(
        chat_id=TARGET_CHAT_ID,
        text=final_text
    )


app = ApplicationBuilder().token(TOKEN).build()

# 🔥 ловимо тільки реальні message updates
app.add_handler(MessageHandler(filters.ALL, forward_message))

print("Bot started...")

app.run_polling()
