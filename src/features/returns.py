import numpy as np
import pandas as pd

def add_log_returns(df:pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.sort_values(['Tickers','Date'])

    df['log_return_1d'] = (
        df.groupby("Ticker")['Close'].transform(lambda x: np.log(x/x.shift(1)))
    )
    
    return df