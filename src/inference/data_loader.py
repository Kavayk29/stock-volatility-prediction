import yfinance as yf
import pandas as pd

def download_stock_data(
        ticker:str,
        period:str="6mo"
)->pd.DataFrame:

    df = yf.download(
        ticker,
        period=period,
        auto_adjust=False,
        progress=False
    )
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
        
    df = df.rename(columns={"Volume":"Volumne"})

    if df.empty:
        raise ValueError(f"No data found for {ticker}")

    df = df.reset_index()

    df['Ticker'] = ticker.upper()

    return df