import pandas as pd

# Load the dataset
df = pd.read_csv("messy_customer_data.csv")  # Ensure this matches the file location

# Display first few rows
print(df.head())

# Get dataset info
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Check for duplicates
print(df.duplicated().sum())


# Standardize column names
df.columns = df.columns.str.strip().str.lower()

# Fill missing values
df['age'].fillna(df['age'].median(), inplace=True)  # Fill missing Age with median
df['email'].fillna("Unknown", inplace=True)  # Fill missing emails with "Unknown"
df['purchase_amount'].fillna(df['purchase_amount'].median(), inplace=True)  # Fill missing purchases

# Convert join_date to datetime format
df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Fix negative values in purchase_amount
df['purchase_amount'] = df['purchase_amount'].apply(lambda x: abs(x) if x < 0 else x)

# Display cleaned dataset
print(df.info())
print(df.head())

# Save cleaned dataset
df.to_csv("cleaned_customer_data.csv", index=False)
print("✅ Data Cleaning Complete! Cleaned dataset saved as 'cleaned_customer_data.csv'")
