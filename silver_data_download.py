import yfinance as yf
import pandas as pd

ticker = "HDFCSILVER.NS"
start_date = "2007-01-01"
end_date = "2025-12-27"

print(f"Downloading data for {ticker}...")
data = yf.download(ticker,start=start_date,end=end_date)

path = "hdfc_silver_etf.csv"
data.to_csv(path)

print(f"data saved to {path}")
