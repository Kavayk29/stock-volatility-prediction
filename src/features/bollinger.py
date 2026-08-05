import pandas as pd

WINDOW=20
NUM_STD = 2


def add_bollinger_bands(df:pd.DataFrame)->pd.DataFrame:

    df = df.copy()

    df = df.sort_values(['Ticker','Date'])

    grouped = df.grouped('Ticker')['Close']

    rolling_mean = grouped.transform(lambda x: x.rolling(WINDOW).mean())

    rolling_std = grouped.transform(lambda x: x.rolling(WINDOW).std())

    upper = rolling_mean + NUM_STD * rolling_std
    lower = rolling_mean - NUM_STD * rolling_std

    df['bollinger_upper'] = upper
    df['bollinger_lower'] = lower

    df['bollinger_bandwidth'] = (
        (upper-lower) / rolling_mean
    )

    df['bollinger_percent_b'] = (
        (df['Close']-lower) / (upper-lower)
    )
    return df