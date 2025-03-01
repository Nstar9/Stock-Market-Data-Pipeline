import yfinance as yf
import pandas as pd
import os

# Define the stock symbol and time range
stock_symbol = "AAPL"  # Apple Stock
start_date = "2023-01-01"
end_date = "2024-01-01"

# Fetch stock data from Yahoo Finance
print(f"Fetching stock data for {stock_symbol} from {start_date} to {end_date}...")
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Save raw stock data
raw_file_path = "raw_stock_data.csv"
stock_data.to_csv(raw_file_path)
print(f"✅ Raw stock data saved as '{raw_file_path}'.")

# Load raw data for cleaning
df = pd.read_csv(raw_file_path)

# Standardize column names
df.columns = df.columns.str.strip().str.lower()

# Handle missing values
df.ffill(inplace=True)  # Forward-fill missing values
df.bfill(inplace=True)  # Backfill missing values


# Save cleaned stock data
cleaned_file_path = "cleaned_stock_data.csv"
df.to_csv(cleaned_file_path, index=False)
print(f"✅ Cleaned stock data saved as '{cleaned_file_path}'.")

