import pandas as pd

df = pd.read_csv("sales_data.csv")

df['Quantity'].fillna(df['Quantity'].median(), inplace=True)
df['Price'].fillna(df['Price'].mean(), inplace=True)

total_sales = df['Total_Sales'].sum()
average_order_value = df['Total_Sales'].mean()
highest_single_order = df['Total_Sales'].max()
best_selling_product = df.groupby('Product')['Quantity'].sum().idxmax()
total_orders = df.shape[0]

print("Total Sales:", total_sales)
print("Best Selling Product:", best_selling_product)
print("Average Order Value:", average_order_value)
print("Highest Single Order Value:", highest_single_order)
print("Total Orders:", total_orders)
