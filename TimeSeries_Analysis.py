import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("cleaned_customer_data.csv")

# Convert 'join_date' to datetime format
df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')

# Extract Year & Month
df['year_month'] = df['join_date'].dt.to_period('M')

# Show dataset structure
print(df.head())
print(df.info())

# Count signups per month
signups_per_month = df.groupby('year_month').size()

# Plot customer signups trend
plt.figure(figsize=(10,5))
signups_per_month.plot(marker='o', linestyle='-', color='blue')
plt.title("Customer Signups Over Time")
plt.xlabel("Year-Month")
plt.ylabel("Number of Signups")
plt.xticks(rotation=45)
plt.grid()
plt.savefig("customer_signups_over_time.png")  # Save the plot
plt.show()


# Sum of purchase amount per month
purchase_trends = df.groupby('year_month')['purchase_amount'].sum()

# Plot total purchases per month
plt.figure(figsize=(10,5))
purchase_trends.plot(marker='o', linestyle='-', color='green')
plt.title("Total Purchase Amount Over Time")
plt.xlabel("Year-Month")
plt.ylabel("Total Purchase Amount ($)")
plt.xticks(rotation=45)
plt.grid()
plt.savefig("purchase_trends_over_time.png")  # Save the plot
plt.show()

# Calculate 3-month moving average for purchases
purchase_trends_ma = purchase_trends.rolling(window=3).mean()

# Plot moving average trend
plt.figure(figsize=(10,5))
purchase_trends.plot(marker='o', linestyle='-', color='green', label="Monthly Purchases")
purchase_trends_ma.plot(marker='o', linestyle='-', color='red', label="3-Month Moving Average")
plt.title("Purchase Trends with Moving Average")
plt.xlabel("Year-Month")
plt.ylabel("Total Purchase Amount ($)")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.savefig("purchase_trends_moving_avg.png")  # Save the plot
plt.show()
