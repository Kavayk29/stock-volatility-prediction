from pathlib import Path
import pandas as pd

INPUT_PATH = Path("data/processed/market_dataset.parquet")
OUTPUT_DIR = Path("data/processed")

TRAIN_END = "2023-12-31"
VALID_END = "2024-12-31"

def main():
    print("Loading model dataset")

    df = pd.read_parquet(INPUT_PATH)

    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(['Date','Ticker']).reset_index(drop=True)

    train_df = df[df['Date']<= TRAIN_END]

    val_df = df[(df['Date']>TRAIN_END) & (df['Date']<=VALID_END)]

    test_df = df[df['Date']> VALID_END]

    train_df.to_parquet(OUTPUT_DIR/"train.parquet",index = False)
    val_df.to_parquet(OUTPUT_DIR/"val.parquet",index=False)
    test_df.to_parquet(OUTPUT_DIR/'test.parquet',index=False)

    print(f"train's shape {train_df.shape}")
    print(f"val shape {val_df.shape}")
    print(f"test shape {test_df.shape}")

    print(
        train_df["Date"].min(),
        train_df["Date"].max()
    )

    print(
        val_df["Date"].min(),
        val_df["Date"].max()
    )

    print(
        test_df["Date"].min(),
        test_df["Date"].max()
    )

if __name__=='__main__':
    main()