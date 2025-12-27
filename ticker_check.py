import yfinance as yf
import pandas as pd

def check_ticker_exists(ticker_symbol):
    """
    Checks if a given ticker symbol exists by attempting to download a small
    amount of historical data.
    """
    print(f"Checking ticker: {ticker_symbol}")
    try:
            # Attempt to download data for a very short period (e.g., 1 day)
            # This is usually enough to determine if the ticker is valid.
            data = yf.download(ticker_symbol, period="1d", progress=False)
            if not data.empty:
                print(f"SUCCESS: Ticker '{ticker_symbol}' exists and data is available.")
                return True
            else:
                print(f"FAIL: Ticker '{ticker_symbol}' does not exist or no data found.")
                return False
    except Exception as e:
        print(f"ERROR: An error occurred while checking '{ticker_symbol}': {e}")
        print(f"This usually means the ticker is invalid or there's a network issue.")
        return False

#Test with the likely correct format for NSE
check_ticker_exists("HDFCSILVER.NS")
#Test with the format you provided (likely won't work directly)
check_ticker_exists("NSE: HDFCSILVER")
# You can also try without any suffix, sometimes yfinance can infer
check_ticker_exists("HDFCSILVER")