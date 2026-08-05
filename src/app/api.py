from fastapi import FastAPI

from src.app.schemas import (
    PredictionRequest,
    PredictionResponse
)

from src.inference.inference_pipeline import run_inference

app = FastAPI(
    title="Stock Volatility Predictions API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "Message": "Stock Volatility Prediction API is running"
    }

@app.post(
    "/predict",
    response_model=PredictionResponse
)

def predict(request: PredictionRequest):
    prediction = run_inference(request.ticker)

    return PredictionResponse(
        ticker=request.ticker.upper(),
        predicted_volatility=float(prediction)
    )