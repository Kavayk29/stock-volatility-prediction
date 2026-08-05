import pandas as pd

df = pd.read_parquet("data/processed/market_dataset.parquet")

print(df.shape)

print(df.isna().sum().sum())
print(df['Ticker'].nunique())

print(df['Date'].min(), df['Date'].max())

print(df.head())