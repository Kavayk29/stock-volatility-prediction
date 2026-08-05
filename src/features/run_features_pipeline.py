from pathlib import Path
import pandas as pd

from src.features.feature_pipeline import build_feature_pipeline

INPUT_PATH = Path("data/processed/market_data_clean.parquet")
OUTPUT_PATH = Path("data/processed/market_features.parquet")

def main():

    print("loading clean data")
    df = pd.read_parquet(INPUT_PATH)

    df = build_feature_pipeline(df)

    print("Saving Features")

    df.to_parquet(OUTPUT_PATH, index=False)
    print("Done")

if __name__=="__main__":
    main()