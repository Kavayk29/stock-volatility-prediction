import pandas as pd

TARGET_WINDOW = 5

def add_future_volatility_target(df:pd.DataFrame)->pd.DataFrame:

    df = df.copy()

    df = df.sort_values(['Ticker','Date'])

    df['future_volatility_5d'] = (
        df.groupby('Ticker')['log_return_1d'].transform(
            lambda x: (
                x.shift(-1).rolling(TARGET_WINDOW).std().shift(-(TARGET_WINDOW-1))
            )
        )
    )

    return df