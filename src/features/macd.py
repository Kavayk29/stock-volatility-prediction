import pandas as pd

FAST_EMA = 12
SLOW_EMA = 26
SIGNAL_EMA = 9

def calculate_macd(close: pd.Series) -> pd.DataFrame:

    ema_fast = close.ewm(span= FAST_EMA,adjust=False).mean()
    ema_slow = close.ewm(span=SLOW_EMA, adjust=False).mean()

    macd = ema_fast - ema_slow

    signal = macd.ewm(span=SIGNAL_EMA,adjust=False).mean()

    histogram = macd-signal

    return pd.DataFrame({
        "macd":macd,
        "macs_signal":signal,
        "macd_histogram":histogram
    })

def add_macd(df:pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    df  =df.sort_values(['Ticker','Date'])

    macd_df = (
        df.groupby('Ticker')['Close'].apply(calculate_macd).reset_index(level=0,drop=True)
    )
    df[['macd','macd_signal','macd_histogram']] = macd_df

    return df