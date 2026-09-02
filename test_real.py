import pandas as pd
from data_fetcher import DataFetcher
from test_strategy import MovingAverageCrossover
from backtester import Backtester

print("Fetching REAL Nifty 50 Data from DhanHQ...")
fetcher = DataFetcher()
# Fetching last 30 days of 1-minute data
df = fetcher.get_historical_data(from_date='2026-08-01', to_date='2026-09-02')

if df.empty:
    print("Failed to fetch real data. Backtest aborted.")
else:
    print(f"Fetched {len(df)} candles! Running backtest...")
    
    # Run the moving average strategy
    strategy = MovingAverageCrossover(fast_period=10, slow_period=30)
    bt = Backtester(df, strategy)
    bt.run()
