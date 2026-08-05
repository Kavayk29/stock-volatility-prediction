import pandas as pd

from src.features.returns import add_log_returns
from src.features.rolling_features import add_rolling_features
from src.features.moving_averages import add_moving_averages
from src.features.momentum import add_rsi
from src.features.macd import add_macd
from src.features.bollinger import add_bollinger_bands
from src.features.volumne import add_volumne_features
from src.features.price_action import add_price_action_features

def build_feature_pipeline(df:pd.DataFrame)->pd.DataFrame:

    print("Creating log returns")
    df = add_log_returns(df)

    print("rolling features")
    df = add_rolling_features(df)

    print("moving avg")
    df = add_moving_averages(df)

    print("rsi")
    df = add_rsi(df)

    print("Creating MACD...")
    df = add_macd(df)

    print("Creating Bollinger Bands...")
    df = add_bollinger_bands(df)

    print("Creating Volume Features...")
    df = add_volumne_features(df)

    print("Creating Price Action Features...")
    df = add_price_action_features(df)

    print("Feature Engineering Complete!")

    return df