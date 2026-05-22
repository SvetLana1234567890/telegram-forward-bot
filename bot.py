from telegram.ext import TypeHandler

async def forward_all(update: Update, context: ContextTypes.DEFAULT_TYPE):

    msg = update.message or update.channel_post or update.edited_message

    if not msg:
        return

    text = msg.text or msg.caption or str(msg.to_dict())

    await context.bot.send_message(
        chat_id=TARGET_CHAT_ID,
        text=f"🏪 {msg.chat.title}\n\n{text}"
    )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(TypeHandler(Update, forward_all))



