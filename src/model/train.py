from pathlib import Path
import joblib

import pandas as pd

from xgboost import XGBRegressor

from sklearn.metrics import (
    mean_absolute_error,
    root_mean_squared_error,
    r2_score,
)

TRAIN_PATH = Path("data/processed/train.parquet")
VALIDATION_PATH = Path("data/processed/val.parquet")

MODEL_DIR = Path("saved_models")
MODEL_DIR.mkdir(exist_ok=True)

MODEL_PATH = MODEL_DIR / "xgboost_model.pkl"

TARGET_COLUMN = "future_volatility_5d"

train_df = pd.read_parquet(TRAIN_PATH)
validation_df = pd.read_parquet(VALIDATION_PATH)

EXCLUDED_COLUMNS = [
    "Date",
    "Ticker",
    TARGET_COLUMN,
]

FEATURE_COLUMNS = [
    col
    for col in train_df.columns
    if col not in EXCLUDED_COLUMNS
]

X_train = train_df[FEATURE_COLUMNS]
y_train = train_df[TARGET_COLUMN]

X_valid = validation_df[FEATURE_COLUMNS]
y_valid = validation_df[TARGET_COLUMN]

model = XGBRegressor(

    objective="reg:squarederror",

    n_estimators=500,

    learning_rate=0.05,

    max_depth=6,

    subsample=0.8,

    colsample_bytree=0.8,

    random_state=42,

    n_jobs=-1,
)

print("Training XGBoost...")

model.fit(
    X_train,
    y_train,
)

predictions = model.predict(X_valid)

mae = mean_absolute_error(y_valid, predictions)

rmse = root_mean_squared_error(
    y_valid,
    predictions,
)

r2 = r2_score(
    y_valid,
    predictions,
)

print("=" * 60)

print(f"MAE  : {mae:.6f}")
print(f"RMSE : {rmse:.6f}")
print(f"R²   : {r2:.6f}")

joblib.dump(model, MODEL_PATH)
joblib.dump(FEATURE_COLUMNS, "saved_models/feature_columns.pkl")

print(f"Model saved to {MODEL_PATH}")