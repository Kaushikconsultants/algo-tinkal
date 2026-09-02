import pandas as pd
import pandas_ta as ta

class StrategyBase:
    def __init__(self, name="BaseStrategy"):
        self.name = name
        
    def generate_signals(self, df):
        """
        Takes a DataFrame with OHLCV data.
        Returns the DataFrame with an additional 'signal' column.
        1 = Buy, -1 = Sell, 0 = Hold
        """
        raise NotImplementedError("Strategies must implement generate_signals method")
