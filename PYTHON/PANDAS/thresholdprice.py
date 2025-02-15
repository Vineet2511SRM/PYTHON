import pandas as pd

# Create the DataFrame
data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Printer'],
    'Price': [800, 20, 50, 150, 120],
    'Quantity': [10, 50, 40, 20, 15]
}
df = pd.DataFrame(data)

# Define the price threshold
price_threshold = 100

# Filter the DataFrame
filtered_df = df[df['Price'] > price_threshold]

print("Filtered DataFrame (Price > threshold):")
print(filtered_df)
