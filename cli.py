import argparse
import os
from bot.client import BinanceTestnetClient
from bot.validators import validate_positive, validate_inputs
from bot.orders import execute_order
from bot.logging_config import logger

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot CLI")
    
    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--quantity", required=True, type=validate_positive, help="Quantity to trade")
    parser.add_argument("--price", type=validate_positive, help="Price (required for LIMIT)")

    args = parser.parse_args()

    # 1. Validate Inputs
    try:
        validate_inputs(args)
    except ValueError as e:
        print(f"Validation Error: {e}")
        return

    # 2. Get API Credentials from Environment Variables
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        print("Error: Please set BINANCE_API_KEY and BINANCE_API_SECRET environment variables.")
        return

    # 3. Initialize Client and Execute
    try:
        bot_client = BinanceTestnetClient(api_key, api_secret).get_client()
        
        print("\n--- Order Request Summary ---")
        print(f"Symbol:   {args.symbol.upper()}")
        print(f"Side:     {args.side.upper()}")
        print(f"Type:     {args.type.upper()}")
        print(f"Quantity: {args.quantity}")
        if args.price: print(f"Price:    {args.price}")
        print("-----------------------------\n")

        response = execute_order(
            bot_client, 
            args.symbol, 
            args.side, 
            args.type, 
            args.quantity, 
            args.price
        )

        print("SUCCESS: Order placed.")
        print(f"Order ID:      {response.get('orderId')}")
        print(f"Status:        {response.get('status')}")
        print(f"Executed Qty:  {response.get('executedQty')}")
        print(f"Avg Price:     {response.get('avgPrice', 'N/A')}")

    except Exception as e:
        print(f"\nFAILED: Could not place order. Check trading_bot.log for details.")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()