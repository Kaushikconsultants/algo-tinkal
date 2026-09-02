import pandas as pd
import numpy as np
from test_strategy import MovingAverageCrossover
from backtester import Backtester

print("Generating mock data to test the backtester...")
# Generate 100 days of mock price data
dates = pd.date_range(start="2026-01-01", periods=100, freq='D')
np.random.seed(42)
prices = 1000 + np.cumsum(np.random.randn(100) * 10)
df = pd.DataFrame({'close': prices}, index=dates)

strategy = MovingAverageCrossover(fast_period=5, slow_period=20)
bt = Backtester(df, strategy)
bt.run()
