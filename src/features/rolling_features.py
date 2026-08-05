import pandas as pd

def add_rolling_features(df:pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    df = df.sort_values(['Ticker','Date'])
    grouped = df.groupby('Ticker')['log_return_1d']

    windows = [5,10,20]

    for window in windows:

        df[f"rolling_mean_{window}"] =( 
            grouped.transform(
            lambda x: x.rolling(window).mean())
        )

        df[f"rolling_std_{window}"] =( 
                    grouped.transform(
                    lambda x: x.rolling(window).std())
        )
    return df