# Binance Futures Testnet Trading Bot

A production-quality CLI tool to interact with the Binance Futures USDT-M Testnet. This bot supports Market, Limit, and Stop-Limit orders with structured logging and input validation.

## Features
- **Supported Order Types**: MARKET, LIMIT, and STOP_LIMIT (Bonus Feature).
- **Environment Management**: Automatic loading of API keys from `.env` files.
- **Validation**: Strict checking of quantity, price, and side (BUY/SELL).
- **Logging**: All requests, API responses, and errors are saved to `trading_bot.log`.

## Setup

1. **Clone the project** and navigate to the root directory.
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt