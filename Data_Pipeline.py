import pandas as pd
import os

# Load raw dataset (simulate extraction from source)
file_path = "raw_customer_data.csv"

# Check if file exists
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    print("✅ Raw data loaded successfully.")
else:
    print("❌ File not found! Creating an empty DataFrame as fallback.")
    df = pd.DataFrame(columns=["customer_id", "name", "age", "email", "purchase_amount", "join_date"])

# Standardize column names
df.columns = df.columns.str.strip().str.lower()

# Fill missing values (only if data exists)
if not df.empty:
    df['age'].fillna(df['age'].median(), inplace=True)
    df['email'].fillna("Unknown", inplace=True)
    df['purchase_amount'].fillna(df['purchase_amount'].median(), inplace=True)

    # Convert join_date to datetime
    df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Fix negative values in purchase_amount
    df['purchase_amount'] = df['purchase_amount'].apply(lambda x: abs(x) if pd.notna(x) and x < 0 else x)

    print("✅ Data cleaning completed.")

# Save cleaned data
cleaned_file_path = "cleaned_customer_data.csv"
df.to_csv(cleaned_file_path, index=False)
print(f"✅ Cleaned data saved as '{cleaned_file_path}'.")
