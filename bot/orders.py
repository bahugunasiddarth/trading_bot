from bot.logging_config import logger
from binance.exceptions import BinanceAPIException

def execute_order(client, symbol, side, order_type, quantity, price=None, stop_price=None):
    """
    Sends the order to Binance Futures Testnet.
    """
    symbol = symbol.upper()
    side = side.upper()
    order_type = order_type.upper()
    
    logger.info(f"Preparing {order_type} {side} order for {symbol} - Qty: {quantity}")

    try:
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            params["price"] = str(price)
            params["timeInForce"] = "GTC"

        # Added logic for STOP_LIMIT
        if order_type == "STOP_LIMIT":
            params["price"] = str(price)
            params["stopPrice"] = str(stop_price)
            params["timeInForce"] = "GTC"

        # Create Futures Order
        response = client.futures_create_order(**params)
        
        logger.info(f"Order Successful. ID: {response.get('orderId')}")
        return response

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e.message} (Code: {e.code})")
        raise
    except Exception as e:
        logger.error(f"Unexpected error executing order: {str(e)}")
        raise