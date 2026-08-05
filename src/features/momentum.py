import numpy as np
import pandas as pd

def calculate_rsi(close:pd.Series, window:int=14)->pd.Series:

    delta = close.diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean()

    rs = avg_gain/avg_loss

    rsi = 100 - (100/(1+rs))

    return rsi

def add_rsi(df:pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    df = df.sort_values(['Ticker','Date'])

    df['rsi_14'] = (
        df.groupby['Tickers']['Close'].transform(calculate_rsi)
    )

    return df