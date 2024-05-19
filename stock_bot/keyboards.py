from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from stock_bot.config import DEFAULT_STOCKS

async def start(update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Welcome to the bot! Please choose a stock or type a custom symbol:",
                                   reply_markup=stock_menu_keyboard())

def stock_menu_keyboard():
    keyboard = []
    for i in range(0, len(DEFAULT_STOCKS), 3):
        row = [
            InlineKeyboardButton(DEFAULT_STOCKS[i], callback_data=DEFAULT_STOCKS[i]) if i < len(DEFAULT_STOCKS) else None,
            InlineKeyboardButton(DEFAULT_STOCKS[i+1], callback_data=DEFAULT_STOCKS[i+1]) if i+1 < len(DEFAULT_STOCKS) else None,
            InlineKeyboardButton(DEFAULT_STOCKS[i+2], callback_data=DEFAULT_STOCKS[i+2]) if i+2 < len(DEFAULT_STOCKS) else None
        ]
        keyboard.append([btn for btn in row if btn is not None])
    keyboard.append([InlineKeyboardButton("Enter custom symbol", callback_data="custom_symbol")])
    return InlineKeyboardMarkup(keyboard)

async def stock_selection(update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "custom_symbol":
        await query.edit_message_text("Please enter the stock symbol:")
    else:
        stock_symbol = query.data
        await query.edit_message_text(f"Selected {stock_symbol}. Choose a duration:", reply_markup=duration_menu_keyboard(stock_symbol))

def duration_menu_keyboard(stock_symbol):
    keyboard = [
        [InlineKeyboardButton("1 minute", callback_data=f'{stock_symbol}_1min')],
        [InlineKeyboardButton("5 minutes", callback_data=f'{stock_symbol}_5min')],
        [InlineKeyboardButton("15 minutes", callback_data=f'{stock_symbol}_15min')],
        [InlineKeyboardButton("30 minutes", callback_data=f'{stock_symbol}_30min')],
        [InlineKeyboardButton("60 minutes", callback_data=f'{stock_symbol}_60min')],
        [InlineKeyboardButton("Daily", callback_data=f'{stock_symbol}_daily')],
        [InlineKeyboardButton("Weekly", callback_data=f'{stock_symbol}_weekly')],
        [InlineKeyboardButton("Monthly", callback_data=f'{stock_symbol}_monthly')],
    ]
    return InlineKeyboardMarkup(keyboard)
