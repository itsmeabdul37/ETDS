import pandas as pd
import numpy as np
import os

data = {
'Transaction_ID': [1, 2, 3, 4, 5],
'Product': ['A', 'B', 'C', 'A', 'B'],
'Quantity': [10, -5, 20, 15, 8],
'Price': [15.0, 20.0, 25.0, None, 30.0],
'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04',
'2023-01-05']
}

df = pd.DataFrame(data)
print("Task 1: Loaded Dataset")
print(df.head())

missing_cols = df.columns[df.isnull().any()]
df. fillna(0, inplace=True)
print("\nTask 2: Missing Values - After Handling")
print(df)

numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].abs()
print("\nfask 3: Negative Values - After Handling")
print(df)

df[ 'Date'] = pd.to_datetime(df['Date'])
print("\nTask 4: Converted 'Date' column to DateTime format")
print(df)

df[ 'Day'] = df['Date'].dt.day
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
print("\nTask 5: Extracted day, month, and year information from 'Date'")
print(df)

df['Total Sales'] = df['Quantity'] * df['Price']
print("\nTask 6: Calculated 'Total Sales'")
print(df)

grouped_df = df.groupby("Product").agg({"Quantity": "sum", "Total Sales":
"sum"}).reset_index()
print("\nTask 7: Grouped and Aggregated Data by 'Product'")
print(grouped_df)

wrangled_file_path = os.path.abspath('wrangled_dataset.csv')
df.to_csv(wrangled_file_path, index=False)
print("\nTask 8: Saved the Wrangled Dataset to", wrangled_file_path)

transformed_file_path = os.path.abspath('transformed_dataset.csv')
df.to_csv(transformed_file_path, index=False)
print("\nTask 9: Saved the Transformed Dataset to",
transformed_file_path)

transposed_df = df.transpose()
transposed_file_path = os.path.abspath("tramsposed dataset.csv")
transposed_df.to_csv(transposed_file_path, header=False)
print("\nTask 10: Transposed Dataset and Saved to", transposed_file_path)

print("\nExample using iloc:")
selected_rows = df.iloc[1:3]
selected_columns = df.iloc[:, [0, 2, 4]]
print("Selected Rows:")
print(selected_rows)
print("Selected Columns:")
print(selected_columns)

sorted_df = df.sort_values(by='Total Sales', ascending=False)
print("\nExample of Sorting by 'Total Sales' in Descending Order:")
print(sorted_df)