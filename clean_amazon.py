import pandas as pd
import re  


df = pd.read_csv("amazon.csv")


df['discounted_price'] = df['discounted_price'].str.replace('[₹$,]', '', regex=True)
df['actual_price'] = df['actual_price'].str.replace('[₹$,]', '', regex=True)


df['discounted_price'] = pd.to_numeric(df['discounted_price'], errors='coerce')
df['actual_price'] = pd.to_numeric(df['actual_price'], errors='coerce')


df['rating_count'] = df['rating_count'].str.replace('[^0-9-]', '', regex=True)


df['rating_count'] = pd.to_numeric(df['rating_count'], errors='coerce').fillna(0)


df['rating_count'] = df['rating_count'].astype(int)


print(df.dtypes)


df.to_csv("amazon_cleaned.csv", index=False)

print("Price and rating_count conversions completed. Cleaned data saved to amazon_cleaned.csv")