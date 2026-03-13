from binance.client import Client
from bot.logging_config import logger

class BinanceTestnetClient:
    def __init__(self, api_key: str, api_secret: str):
        """
        Initializes the Binance Client for Futures Testnet.
        """
        if not api_key or not api_secret:
            logger.error("API Key or Secret missing.")
            raise ValueError("API Key and Secret are required.")
            
        self.client = Client(api_key, api_secret, testnet=True)
        # Point to the specific Futures Testnet URL
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi/v1'
        
        logger.info("Binance Testnet Client initialized successfully.")

    def get_client(self):
        return self.client