from pathlib import Path

import joblib
import pandas as pd

MODEL_PATH = Path("models/xgboost/xgboost_model.pkl")
FEATURE_PATH = Path("models/xgboost/feature_columns.pkl")

class VolatilityPredictor:

    def __init__(self):
        self.model = joblib.load(MODEL_PATH)
        self.feature_columns = joblib.load(FEATURE_PATH)

    def predict(self,df:pd.DataFrame):

        X = df[self.feature_columns]
        predictions = self.model.predict(X)

        return predictions