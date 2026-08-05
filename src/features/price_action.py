import numpy as np
import pandas as pd

def add_price_action_features(df:pd.DataFrame)-> pd.DataFrame:

    df = df.copy()

    df['high_low_range'] = (
        (df['High']-df['Low'])/df['Close']
    )

    df['open_close_return'] = (
        (df['Close']-df['Open'])/df['Open']
    )

    df['body_size'] = (
        np.abs(df['Close']-df['Open'])/df['Open']
    )

    df['upper_shadow'] = (
        (df['High']-df[['Open','Close']].max(axis=1))/df['Close']
    )

    df['lower_shadow'] = (
        (df[['Open', 'Close']].min(axis=1)-df['Low'])
        / df['Close']
    )

    return df