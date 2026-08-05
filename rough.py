import numpy as np
import pandas as pd


path = "data/processed/market_dataset.parquet"

df = pd.read_parquet(path)


print("Before:")
print(np.isinf(df["volumne_chanage_1d"]).sum())


df["volumne_chanage_1d"] = (
    df["volumne_chanage_1d"]
    .replace([np.inf, -np.inf], np.nan)
    .fillna(0)
)


print("After:")
print(np.isinf(df["volumne_chanage_1d"]).sum())


df.to_parquet(
    path,
    index=False
)

print("Saved successfully")