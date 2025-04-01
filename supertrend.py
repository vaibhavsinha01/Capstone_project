import pandas as pd
from ta.volatility import AverageTrueRange
from ta.trend import EMAIndicator,MACD
from ta.momentum import RSIIndicator
import time

class Trade:
    def __init__(self):
        self.df = pd.read_csv(r"C:\Users\vaibh\OneDrive\Desktop\capstone\Capstone_project\RELIANCE_NSE_day.csv")
        self.df['Signal'] = 0

    def calculate_indicators(self):
        atr = AverageTrueRange(high=self.df['high'], low=self.df['low'], close=self.df['close'], window=10)
        self.df['ATR'] = atr.average_true_range()
        self.df['ATRL'] = self.df['close'] - 3 * self.df['ATR']
        self.df['ATRH'] = self.df['close'] + 3 * self.df['ATR']
        ema = EMAIndicator(close=self.df['close'], window=100)
        self.df['EMA100'] = ema.ema_indicator()

    def generate_signals(self):
        for i in range(1, len(self.df)):
            if self.df.loc[i - 1, 'close'] < self.df.loc[i, 'ATRL'] and self.df.loc[i, 'close'] < self.df.loc[i, 'EMA100']:
                self.df.loc[i, 'Signal'] = 1
            elif self.df.loc[i - 1, 'close'] > self.df.loc[i, 'ATRH'] and self.df.loc[i, 'close'] > self.df.loc[i, 'EMA100']:
                self.df.loc[i, 'Signal'] = -1
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
            self.calculate_indicators()
            self.generate_signals()
            self.execute_trade()

if __name__ == "__main__":
    trade_bot = Trade()
    while True:
        trade_bot.run_strategy()
        time.sleep(60)
