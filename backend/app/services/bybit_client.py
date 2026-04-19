from pybit.unified_trading import HTTP
from decimal import Decimal
import os

class BybitClient:
    def __init__(self):
        self.session = HTTP(
            testnet=False,
            api_key=os.getenv("BYBIT_API_KEY"),
            api_secret=os.getenv("BYBIT_API_SECRET"),
        )

    def get_ticker(self, symbol: str):
        response = self.session.get_tickers(
            category="linear",
            symbol=symbol.upper()
        )
        if response.get("retCode") == 0:
            data = response["result"]["list"][0]
            return {
                "symbol": data["symbol"],
                "price": float(data["lastPrice"]),
                "volume_24h": float(data.get("volume24h", 0))
            }
        return None

    def get_orderbook(self, symbol: str):
        response = self.session.get_orderbook(
            category="linear",
            symbol=symbol.upper()
        )
        if response.get("retCode") == 0:
            asks = response['result']['a']
            bids = response['result']['b']
            return {
                "symbol": symbol,
                "best_ask": float(asks[0][0]) if asks else None,
                "best_bid": float(bids[0][0]) if bids else None,
                "spread": float(asks[0][0]) - float(bids[0][0]) if asks and bids else None
            }
        return None