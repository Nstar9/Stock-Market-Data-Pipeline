import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned stock data
df = pd.read_csv("cleaned_stock_data.csv")
df.index = pd.to_datetime(df.index)  # Convert index to datetime
print(df.columns)  # Check available column names

# Plot stock price trendplt.plot(df.index, df["Close"], label="Stock Price", color="blue"
plt.figure(figsize=(10, 5))
plt.plot(df.index, df["close"], label="Stock Price", color="blue")  # Change to lowercase
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.title("Stock Price Trend")
plt.legend()
plt.grid(True)
plt.show()
