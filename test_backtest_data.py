import os
import pandas as pd
from dhanhq import dhanhq

client_id = "1105806559"
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyUmVnaW9uIjoiUjEiLCJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzg4NDU1MDAwLCJpYXQiOjE3ODgzNjg2MDAsInRva2VuQ29uc3VtZXJUeXBlIjoiU0VMRiIsIndlYmhvb2tVcmwiOiIiLCJkaGFuQ2xpZW50SWQiOiIxMTA1ODA2NTU5In0.1VvA8tKLMfn7jxGRFbqVdCZrbkcCVrraYEbqR8FS_cvJ_gsiM6L7Z88mGLrNePxKi3WK5erjQNNubD8TFyRFGg"

print("Authenticating with DhanHQ...")
try:
    dhan = dhanhq(client_id, access_token)
    
    # Let's test by fetching historical data for Nifty 50 (Security ID 13 for NSE index)
    # Using a recent date range
    print("Fetching historical data for Nifty 50 (1 minute timeframe)...")
    
    historical_data = dhan.get_historical_ohlc(
        symbol='NIFTY 50',
        exchange_segment='IDX_I',
        instrument_type='INDEX',
        expiry_code=0,
        from_date='2026-08-01',
        to_date='2026-09-02'
    )
    
    if historical_data['status'] == 'success':
        df = pd.DataFrame(historical_data['data'])
        print(f"Success! Fetched {len(df)} candles.")
        print(df.head())
    else:
        print(f"Failed to fetch data: {historical_data}")
        
except Exception as e:
    print(f"Error: {e}")
