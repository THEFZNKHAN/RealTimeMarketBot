import configparser

config = configparser.ConfigParser()
config.read("config/config.ini")

BOT_TOKEN = config["TelegramAPI"]["bot_token"]
BOT_NAME = config["TelegramAPI"]["bot_name"]
STOCK_API_KEY = config["StockAPI"]["api_key"]
BASE_URL = config["StockAPI"]["stock_url"]

DEFAULT_STOCKS = [
    "AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "META", "NVDA",
    "JPM", "GS", "BAC", "WFC", "C", "JNJ", "PFE", "MRK", "UNH",
    "ABBV", "PG", "KO", "PEP", "NKE", "WMT", "XOM", "CVX", "COP",
    "BP", "DUK", "D", "NEE", "SO", "ED", "HD",
    "COST", "TGT", "T", "VZ", "CMCSA", "DIS", "NFLX"
]
