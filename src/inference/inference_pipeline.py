from src.inference.data_loader import download_stock_data
from src.inference.predictor import VolatilityPredictor
from src.features.feature_pipeline import build_feature_pipeline

predictor = VolatilityPredictor()

def run_inference(ticker:str):
    df = download_stock_data(ticker)
    df = build_feature_pipeline(df)
    latest_row = df.tail(1)
    prediction = predictor.predict(latest_row)

    return prediction[0]