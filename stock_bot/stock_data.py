import requests
from telegram import Update
from telegram.ext import ContextTypes
from stock_bot.config import STOCK_API_KEY, BASE_URL
from stock_bot.keyboards import duration_menu_keyboard, stock_menu_keyboard
import logging

logger = logging.getLogger(__name__)

async def fetch_stock_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    stock_symbol, duration = query.data.split('_')
    
    function_mapping = {
        "1min": "TIME_SERIES_INTRADAY",
        "5min": "TIME_SERIES_INTRADAY",
        "15min": "TIME_SERIES_INTRADAY",
        "30min": "TIME_SERIES_INTRADAY",
        "60min": "TIME_SERIES_INTRADAY",
        "daily": "TIME_SERIES_DAILY",
        "weekly": "TIME_SERIES_WEEKLY",
        "monthly": "TIME_SERIES_MONTHLY"
    }
    
    interval_mapping = {
        "1min": "1min",
        "5min": "5min",
        "15min": "15min",
        "30min": "30min",
        "60min": "60min"
    }
    
    function = function_mapping[duration]
    params = {
        "function": function,
        "symbol": stock_symbol,
        "apikey": STOCK_API_KEY
    }
    
    if duration in interval_mapping:
        params["interval"] = interval_mapping[duration]
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        if "Error Message" in data:
            await query.edit_message_text("Invalid API call. Please try again later.")
            return
        
        time_series_key = {
            "1min": "Time Series (1min)",
            "5min": "Time Series (5min)",
            "15min": "Time Series (15min)",
            "30min": "Time Series (30min)",
            "60min": "Time Series (60min)",
            "daily": "Time Series (Daily)",
            "weekly": "Weekly Time Series",
            "monthly": "Monthly Time Series"
        }[duration]
        
        time_series = data.get(time_series_key, {})
        if not time_series:
            await query.edit_message_text("No data available for the selected duration.")
            return

        recent_date = list(time_series.keys())[0]
        recent_data = time_series[recent_date]
        open_stock = recent_data['1. open']
        high = recent_data['2. high']
        low = recent_data['3. low']
        close = recent_data['4. close']
        volume = recent_data['5. volume']
        
        message = (f"Stock: {stock_symbol}\n"
                   f"Date: {recent_date}\n"
                   f"Open: {open_stock}\n"
                   f"High: {high}\n"
                   f"Low: {low}\n"
                   f"Close: {close}\n"
                   f"Volume: {volume}")
        
        await query.edit_message_text(message)
        await query.message.reply_text("Please choose another stock or type a custom symbol:", reply_markup=stock_menu_keyboard())

    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching stock data: {e}")
        await query.edit_message_text("Failed to fetch stock data. Please try again later.")

async def handle_custom_symbol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    custom_symbol = update.message.text.strip().upper()
    if custom_symbol:
        await update.message.reply_text(f"Selected custom stock: {custom_symbol}. Choose a duration:",
                                        reply_markup=duration_menu_keyboard(custom_symbol))
