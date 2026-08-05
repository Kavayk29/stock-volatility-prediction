from pathlib import Path
from typing import List

import pandas as pd
import yfinance as yf

DATA_DIR = Path("data/raw")
OUTPUT_FILE = DATA_DIR/"market.parquet"

TICKERS =  [
    "AAPL", "MSFT", "NVDA", "AMZN", "META",
    "GOOGL", "TSLA", "AMD", "NFLX", "ORCL",
    "JPM", "GS", "BAC", "WFC", "MS",
    "JNJ", "PFE", "ABBV", "MRK",
    "WMT", "COST", "HD", "TGT",
    "XOM", "CVX",
    "AVGO", "QCOM", "TXN"
]

START_DATE = "2010-01-01"

def download_market_data(
        tickers:List[str],
        start_date:str,
) -> pd.DataFrame:

    df = yf.download(
        tickers=tickers,
        start = start_date,
        auto_adjust = False,
        group_by='tickers',
        progress=True,
        threads=True
    )
    print(df)

    frames = []

    for ticker in tickers:
        stock_df = df[ticker].copy()
        stock_df = stock_df.reset_index()
        stock_df['Tickers'] = ticker
        frames.append(stock_df)
    market_df = pd.concat(frames,ignore_index=True)

    market_df.columns = [
        'Date',
        'Open',
        'High',
        'Low',
        'Close',
        'Adj Close',
        'Volumne',
        'Ticker'
    ]

    return market_df

def save_data(df: pd.DataFrame) -> None:

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    df.to_parquet(
        OUTPUT_FILE,
        index=False
    )

def main():

    market_df = download_market_data(
        tickers=TICKERS,
        start_date = START_DATE
    )

    save_data(market_df)
    

    print(f"Saved dataset to {OUTPUT_FILE}")

if __name__== "__main__":
    main()