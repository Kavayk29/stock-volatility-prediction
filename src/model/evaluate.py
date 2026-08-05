from pathlib import Path

import joblib
import pandas as pd

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


MODEL_PATH = Path("saved_models/xgboost_model.pkl")

TEST_PATH = Path("data/processed/test.parquet")

TARGET_COLUMN = "future_volatility_5d"


def main():

    print("Loading model...")
    model = joblib.load(MODEL_PATH)


    print("Loading test data...")
    test_df = pd.read_parquet(TEST_PATH)


    excluded_columns = [
        "Date",
        "Ticker",
        TARGET_COLUMN
    ]


    feature_columns = [
        col
        for col in test_df.columns
        if col not in excluded_columns
    ]


    X_test = test_df[feature_columns]

    y_test = test_df[TARGET_COLUMN]


    print("Generating predictions...")

    predictions = model.predict(X_test)


    mae = mean_absolute_error(
        y_test,
        predictions
    )

    rmse = mean_squared_error(
        y_test,
        predictions
    ) ** 0.5


    r2 = r2_score(
        y_test,
        predictions
    )


    print("=" * 60)

    print(f"MAE  : {mae:.6f}")
    print(f"RMSE : {rmse:.6f}")
    print(f"R2   : {r2:.6f}")

    print("=" * 60)


    results = test_df[
        [
            "Date",
            "Ticker",
            TARGET_COLUMN
        ]
    ].copy()

    results["prediction"] = predictions


    results.to_parquet(
        "data/processed/xgboost_test_predictions.parquet",
        index=False
    )


    print("Predictions saved.")


if __name__ == "__main__":
    main()