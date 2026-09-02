import pandas as pd
import pandas_ta as ta
from strategy_base import StrategyBase

class MovingAverageCrossover(StrategyBase):
    def __init__(self, fast_period=10, slow_period=30):
        super().__init__(name=f"MA_Crossover_{fast_period}_{slow_period}")
        self.fast_period = fast_period
        self.slow_period = slow_period
        
    def generate_signals(self, df):
        # Calculate moving averages
        df['fast_ma'] = ta.sma(df['close'], length=self.fast_period)
        df['slow_ma'] = ta.sma(df['close'], length=self.slow_period)
        
        # Generate signals
        df['signal'] = 0
        
        # Buy when fast MA crosses above slow MA
        df.loc[(df['fast_ma'] > df['slow_ma']) & (df['fast_ma'].shift(1) <= df['slow_ma'].shift(1)), 'signal'] = 1
        
        # Sell when fast MA crosses below slow MA
        df.loc[(df['fast_ma'] < df['slow_ma']) & (df['fast_ma'].shift(1) >= df['slow_ma'].shift(1)), 'signal'] = -1
        
        return df
