from pathlib import Path
import pandas as pd

RAW_DATA_PATH = Path("data/raw/market.parquet")
PROCESSED_DATA_DIR = Path("data/processed")
OUTPUT_PATH = PROCESSED_DATA_DIR/"market_data_clean.parquet"

def load_data() -> pd.DataFrame:
    return pd.read_parquet(RAW_DATA_PATH)

def remove_duplicates(df:pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    required_columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Volumne"
    ]
    df = df.dropna(subset=required_columns)

    return df

def correct_dtypes(df:pd.DataFrame) -> pd.DataFrame:

    df["Date"] = pd.to_datetime(df["Date"])

    numeric_columns = [
        "Open",
        "High",
        "Low",
        "Close",
        "Adj Close",
        "Volumne",
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col])

    return df

def sort_data(df:pd.DataFrame) -> pd.DataFrame:
    return (
        df.sort_values(
            ['Ticker','Date']
        ).reset_index(drop=True)
    )

def sanity_checks(df:pd.DataFrame) -> pd.DataFrame:
        assert (df["High"] >= df["Low"]).all()

        assert (df["Open"] > 0).all()

        assert (df["Close"] > 0).all()

        assert (df["Volumne"] >= 0).all()

        assert (
        df.duplicated(["Ticker", "Date"]).sum() == 0
        )

def save_data(df: pd.DataFrame):

    PROCESSED_DATA_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_parquet(
        OUTPUT_PATH,
        index=False,
    )


def main():

    df = load_data()

    df = remove_duplicates(df)

    df = handle_missing_values(df)

    df = correct_dtypes(df)

    df = sort_data(df)

    sanity_checks(df)

    save_data(df)

    print(df.head())
    print(df.shape)


if __name__ == "__main__":
    main()