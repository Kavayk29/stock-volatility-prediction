from pathlib import Path
import pandas as pd

from src.targets.target_generation import add_future_volatility_target

INPUT_PATH = Path("data/processed/market_features.parquet")
OUTPUT_PATH = Path("data/processed/market_dataset.parquet")

def main():
    print("Loading feature dataset")

    df = pd.read_parquet(INPUT_PATH)

    df = add_future_volatility_target(df)

    df = df.dropna()

    df.to_parquet(OUTPUT_PATH,index=False)

if __name__=="__main__":
    main()