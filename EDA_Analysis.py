import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("cleaned_customer_data.csv")

# Display first few rows
print("🔹 First 5 rows of the dataset:")
print(df.head())

# Summary statistics of numerical columns
print("\n🔹 Summary Statistics:")
print(df.describe())

# Check dataset info
print("\n🔹 Dataset Info:")
print(df.info())

# Handling datetime conversion
df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')

# 🔥 STEP 1: DISTRIBUTION ANALYSIS

# Histogram for Age
plt.figure(figsize=(8,4))
sns.histplot(df['age'], bins=10, kde=True, color='blue')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.savefig("age_distribution.png")  # Save the plot
plt.show()

# Histogram for Purchase Amount
plt.figure(figsize=(8,4))
sns.histplot(df['purchase_amount'], bins=10, kde=True, color='green')
plt.title("Purchase Amount Distribution")
plt.xlabel("Purchase Amount ($)")
plt.ylabel("Frequency")
plt.savefig("purchase_amount_distribution.png")  # Save the plot
plt.show()

# 🔥 STEP 2: CORRELATION ANALYSIS

# Select only numeric columns
numeric_df = df.select_dtypes(include=['number'])

# Compute the correlation matrix
correlation_matrix = numeric_df.corr()

# Plot the correlation heatmap
plt.figure(figsize=(8,5))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")  # Save the plot
plt.show()

# 🔥 STEP 3: TIME-BASED ANALYSIS

# Extract Year from Join Date
df['year_joined'] = df['join_date'].dt.year

# Customer signups per year
plt.figure(figsize=(8,4))
sns.countplot(x=df['year_joined'], palette="viridis")
plt.title("Customer Signups Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Customers")
plt.savefig("customer_signups_trend.png")  # Save the plot
plt.show()

# Purchase trends over time
purchase_trends = df.groupby('year_joined')['purchase_amount'].sum()

# Plot purchase trends
plt.figure(figsize=(8,4))
purchase_trends.plot(marker='o', linestyle='-', color='red')
plt.title("Total Purchase Amount Per Year")
plt.xlabel("Year")
plt.ylabel("Total Purchase Amount ($)")
plt.grid()
plt.savefig("purchase_trends.png")  # Save the plot
plt.show()

print("\n✅ EDA Completed! All plots saved successfully.")
