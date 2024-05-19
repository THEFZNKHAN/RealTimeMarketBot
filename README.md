# RealTimeMarketBot

This Telegram bot allows users to fetch real-time stock data directly within Telegram. Users can select from a list of predefined stocks or enter a custom stock symbol to retrieve relevant information such as open, high, low, and close prices, and volume.

## Features

- **Predefined Stocks**: Choose from a list of essential stocks such as AAPL, GOOGL, MSFT, and more.
- **Custom Stock Symbols**: Enter custom stock symbols to fetch data for publicly traded companies.
- **Multiple Durations**: Select from various durations including 1 minute, 5 minutes, 15 minutes, 30 minutes, 60 minutes, daily, weekly, and monthly.
- **Interactive Interface**: User-friendly interface with inline keyboards for easy navigation.
- **Real-time Data**: Fetches real-time stock data from an external API.

## Requirements

- Python 3.8+
- The following Python packages:
  - `python-telegram-bot`
  - `requests`
  - `configparser`

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/THEFZNKHAN/RealTimeMarketBot
   cd RealTimeMarketBot
    ```
2. **Create a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
    ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Configure the bot:**
    - Create a configuration file config/config.ini with the following content
    ```bash
    [TelegramAPI]
    bot_token = YOUR_TELEGRAM_BOT_TOKEN
    bot_name = YOUR_BOT_NAME

    [StockAPI]
    api_key = YOUR_ALPHA_VANTAGE_API_KEY
    stock_url = https://www.alphavantage.co/query
    ```
5. **Running the Bot:**
    ```bash
    python main.py
    ```

## Contributing

Feel free to submit issues, fork the repository, and send pull requests. We welcome contributions from the community!

## Live Demo

[RealTimeMarketBot](https://t.me/RealTimeMarketBot)
