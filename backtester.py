import pandas as pd
import matplotlib.pyplot as plt

class Backtester:
    def __init__(self, df, strategy, initial_capital=100000):
        self.df = df
        self.strategy = strategy
        self.initial_capital = initial_capital
        
    def run(self):
        print(f"Running backtest for {self.strategy.name}...")
        
        # Generate signals
        self.df = self.strategy.generate_signals(self.df)
        
        # Simple backtest logic (assuming we go long on 1 and flat on -1)
        # We track positions: 1 for long, 0 for flat
        self.df['position'] = self.df['signal'].replace(0, pd.NA).ffill().fillna(0)
        # Convert -1 to 0 since we're only going long
        self.df['position'] = self.df['position'].apply(lambda x: 0 if x == -1 else x)
        
        # Calculate returns
        self.df['returns'] = self.df['close'].pct_change()
        self.df['strategy_returns'] = self.df['position'].shift(1) * self.df['returns']
        
        # Calculate equity curve
        self.df['equity'] = self.initial_capital * (1 + self.df['strategy_returns']).cumprod()
        
        self.print_stats()
        self.plot_equity()
        
    def print_stats(self):
        total_return = (self.df['equity'].iloc[-1] - self.initial_capital) / self.initial_capital * 100
        print(f"Total Return: {total_return:.2f}%")
        
    def plot_equity(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.df.index, self.df['equity'], label='Equity Curve')
        plt.title(f"Backtest Results: {self.strategy.name}")
        plt.xlabel("Date")
        plt.ylabel("Capital")
        plt.legend()
        plt.grid()
        plt.savefig("equity_curve.png")
        print("Saved equity curve to equity_curve.png")
