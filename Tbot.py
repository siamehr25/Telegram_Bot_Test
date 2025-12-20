import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Replace 'YOUR_BOT_TOKEN' with your actual token
BOT_TOKEN = "330577938:AAGXd3C-Lt23kUXpF27C1Q9m6CheV077OWQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your bot. 🚀")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"You said:2 {update.message.text}")

def main():
    # Create Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("echo", echo))

    # Start the bot
    print("Bot is running locally... Press Ctrl+C to stop.")
    application.run_polling()

if __name__ == "__main__":
    main()
