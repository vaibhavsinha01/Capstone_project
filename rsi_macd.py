import pandas as pd
from ta.volatility import AverageTrueRange
from ta.trend import EMAIndicator, MACD
from ta.momentum import RSIIndicator
import time

class Trade:
    def __init__(self):
        self.df = pd.read_csv(r"C:\Users\vaibh\OneDrive\Desktop\capstone\Capstone_project\RELIANCE_NSE_day.csv")
        self.df['Signal'] = 0

    def calculate_indicators(self):
        # ATR (Average True Range)
        atr = AverageTrueRange(high=self.df['high'], low=self.df['low'], close=self.df['close'], window=10)
        self.df['ATR'] = atr.average_true_range()
        self.df['ATRL'] = self.df['close'] - 3 * self.df['ATR']
        self.df['ATRH'] = self.df['close'] + 3 * self.df['ATR']
        
        # EMA (Exponential Moving Average)
        ema = EMAIndicator(close=self.df['close'], window=100)
        self.df['EMA100'] = ema.ema_indicator()
        
        # RSI (Relative Strength Index)
        rsi = RSIIndicator(close=self.df['close'], window=14)
        self.df['RSI'] = rsi.rsi()
        
        # MACD (Moving Average Convergence Divergence)
        macd = MACD(close=self.df['close'], window_slow=26, window_fast=12, window_sign=9)
        self.df['MACD'] = macd.macd()
        self.df['MACD_signal'] = macd.macd_signal()

    def generate_signals(self):
        for i in range(1, len(self.df)):
            # Buy Condition: RSI < 30 and MACD Fast crosses above MACD Slow
            if self.df.loc[i, 'RSI'] < 30 and self.df.loc[i, 'MACD'] > self.df.loc[i, 'MACD_signal'] and self.df.loc[i - 1, 'MACD'] <= self.df.loc[i - 1, 'MACD_signal']:
                self.df.loc[i, 'Signal'] = 1  # Buy signal
            
            # Sell Condition: RSI > 70 and MACD Fast crosses below MACD Slow
            elif self.df.loc[i, 'RSI'] > 70 and self.df.loc[i, 'MACD'] < self.df.loc[i, 'MACD_signal'] and self.df.loc[i - 1, 'MACD'] >= self.df.loc[i - 1, 'MACD_signal']:
                self.df.loc[i, 'Signal'] = -1  # Sell signal

            # No action
            else:
                self.df.loc[i, 'Signal'] = 0

    def execute_trade(self):
        if self.df['Signal'].iloc[-1] == 1:
            print("Placing a buy order...")
        elif self.df['Signal'].iloc[-1] == -1:
            print("Placing a sell order...")
        else:
            print("No order placed.")

    def run_strategy(self):
        while True:
            self.calculate_indicators()  # Calculate technical indicators
            self.generate_signals()      # Generate buy/sell signals
            self.execute_trade()         # Execute buy/sell action
            time.sleep(60)               # Wait for the next iteration (1 minute)

if __name__ == "__main__":
    trade_bot = Trade()
    while True:
        trade_bot.run_strategy()
        time.sleep(60)  # Wait for 1 minute before next iteration (this simulates a live trading bot)
