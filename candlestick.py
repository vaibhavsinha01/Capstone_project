import pandas as pd
import numpy as np
from broker_wrapper import AngelBrokerWrapper
import creds
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time

class Strategy:
    def __init__(self):
        # self.current_df = pd.read_csv(r"C:\Users\vaibh\OneDrive\Desktop\ribbon\t3-ribbon\current_orders.csv")
        self.current_df = None
        self.h_pos = 0  # Position status: 0 = no position, 1 = long, -1 = short
        self.last_trade_direction = None  # Direction of last trade: 'BUY' or 'SELL'
        self.trade_multiplier = 1  # Initial trade multiplier (X1)
        self.fake_trade_losses = []  # Stack to store fake trade losses
        # self.balance = self.broker.get_account_balance() # not sure if i can add it here or not the code should work fine either way
        self.fake_trade_losses_amnt = 0 # total loss incurred
        self.complete_orderids = [250401000137702,250401000137758,250401000156281,250401000156334,250401000178580,250401000178619,250401000178591,250401000156313,250401000137735]
        # self.complete_orderids = []
        self.completed_stoploss_ids = []
        # self.completed_stoploss_ids = []
        # self.complete_orderids = []
        self.df = None  # Initialize the dataframe
        self.max_sl = 2
        self.stoploss_orders = [250401000137735, 250401000156313, 250401000178591]
        # self.stoploss_orders = []
        self.martingle_loss_multiplier = 1
    
    def fetch_data(self):
        try:
            current_time = datetime.now()
            market_open_time = current_time.replace(hour=9, minute=30, second=0, microsecond=0)
            start_time = market_open_time - timedelta(days=creds.use_data_for_x_days)
            self.df = self.broker.get_candle_data(
                creds.exchange,
                creds.token_id,
                creds.timeframe,
                start_time.strftime("%Y-%m-%d %H:%M"),
                current_time.strftime("%Y-%m-%d %H:%M")
            )
            if self.df is None or self.df.empty:
                print("Fetched data is empty. Check data source.")
            else:
                print(f"Data fetched successfully: {self.df.tail()}")
        except Exception as e:
            print(f"Error in fetch_data: {e}")
        
    def test(self):
        try:
            api_key = creds.api_key
            username = creds.username
            password = creds.password
            token = creds.token
            self.broker = AngelBrokerWrapper(api_key=api_key, username=username, password=password, token=token)
            print("Broker initialized successfully.")

            self.fetch_data()

        except Exception as e:
            print(f"Error in run: {e}")

if __name__ == "__main__":
    strategy = Strategy()
    # strategy.run()
    strategy.test()
    # strategy.token_download_run()