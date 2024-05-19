from stock_bot.handlers import setup_handlers
from stock_bot.config import BOT_TOKEN
from telegram.ext import Application

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    setup_handlers(app)
    print("Polling...")
    app.run_polling()

if __name__ == "__main__":
    main()