import pandas as pd

def add_volumne_features(df:pd.DataFrame)->pd.DataFrame:

    df = df.copy()
    df = df.sort_values(['Ticker','Date'])
    grouped = df.groupby('Ticker')['Volumne']

    #daily percentage change in volumne
    df['volumne_chanage_1d'] = grouped.transform(lambda x: x.pct_change()
    )

    #rolling stats
    df['volumne_sma_5'] = grouped.transform(
        lambda x: x.rolling(5).mean()
    )

    df['volumne_sma_20'] = grouped.transform(
        lambda x:x.rolling(20).mean()
    )

    df['volumne_std_20'] = grouped.transform(
        lambda x:x.rolling(20).std()
    )

    #relative volumne

    df['relative_volumne_20'] = (
        df['Volumne'] / df['volumne_sma_20']
    )

    df['volumne_zscore_20'] = (
        (df['Volumne'] - df['volumne_sma_20']) / df['volumne_std_20']
    )

    return df