from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from stock_bot.stock_data import fetch_stock_data, handle_custom_symbol
from stock_bot.keyboards import start, stock_selection
from stock_bot.config import BOT_TOKEN, DEFAULT_STOCKS

def setup_handlers(app):
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(stock_selection, pattern='^(' + '|'.join(DEFAULT_STOCKS) + '|custom_symbol)$'))
    app.add_handler(CallbackQueryHandler(fetch_stock_data, pattern='^(' + '|'.join(DEFAULT_STOCKS) + '|[A-Z]+)_(1min|5min|15min|30min|60min|daily|weekly|monthly)$'))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_custom_symbol))

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    setup_handlers(app)
    print("Polling...")
    app.run_polling()

if __name__ == "__main__":
    main()
