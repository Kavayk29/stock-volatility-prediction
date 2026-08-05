from pydantic import BaseModel

class PredictionRequest(BaseModel):
    ticker:str

class PredictionResponse(BaseModel):
    ticker:str
    predicted_volatility:float