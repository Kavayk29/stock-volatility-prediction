import joblib
import pandas as pd

MODEL_PATH = "saved_models/xgboost_model.pkl"


model = joblib.load(MODEL_PATH)


importance = pd.DataFrame(
    {
        "feature": model.feature_names_in_,
        "importance": model.feature_importances_
    }
)


importance = (
    importance
    .sort_values(
        "importance",
        ascending=False
    )
)


print(importance.head(20))