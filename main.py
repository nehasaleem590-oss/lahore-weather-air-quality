from fastapi import FastAPI
from pydantic import BaseModel
import joblib, pandas as pd

app = FastAPI()
model = joblib.load("aqi_model_24h.pkl")
feats = joblib.load("features.pkl")

class Data(BaseModel):
    hour: int
    pm2_5: float
    pm10: float
    aqi_lag1: float
    aqi_lag24: float

@app.post("/predict")
def predict(d: Data):
    X = pd.DataFrame([d.model_dump()])[feats]
    return {"aqi_24h_later": float(model.predict(X)[0])}