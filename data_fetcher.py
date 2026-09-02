import os
import pandas as pd
from dhanhq import DhanContext, dhanhq
from dotenv import load_dotenv

load_dotenv()

class DataFetcher:
    def __init__(self):
        client_id = os.getenv("DHAN_CLIENT_ID")
        access_token = os.getenv("DHAN_ACCESS_TOKEN")
        
        self.context = DhanContext(client_id, access_token)
        self.dhan = dhanhq(self.context)
        
    def get_historical_data(self, security_id='13', exchange_segment='IDX_I', instrument_type='INDEX', from_date='2026-08-01', to_date='2026-09-02'):
        print(f"Fetching real historical data for security {security_id}...")
        
        response = self.dhan.intraday_minute_data(
            security_id=security_id,
            exchange_segment=exchange_segment,
            instrument_type=instrument_type,
            from_date=from_date,
            to_date=to_date
        )
        
        if response.get('status') == 'success':
            df = pd.DataFrame(response['data'])
            if not df.empty:
                df['start_Time'] = pd.to_datetime(df['start_Time'])
                df.set_index('start_Time', inplace=True)
                df = df.sort_index()
            return df
        else:
            print(f"Error fetching data: {response}")
            return pd.DataFrame()

if __name__ == '__main__':
    fetcher = DataFetcher()
    df = fetcher.get_historical_data()
    print(df.head())
    if not df.empty:
        df.to_csv("real_nifty_50.csv")
        print("Saved to real_nifty_50.csv")
