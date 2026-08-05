import pandas as pd

def add_moving_averages(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    df = df.sort_values(['Ticker','Date'])

    grouped = df.groupby('Ticker')['Close']

    windows = [5,10,20,50]

    for window in windows:
        df[f"sma_{window}"] = (
            grouped.transform(
                lambda x: x.rolling(window).mean()
            )
        )
        df[f"ewa_{window}"] = (
            grouped.transform(
                lambda x : x.ewm(
                    span=window,
                    adjust=False
                ).mean()
            )
        )
    return df