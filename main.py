from fastapi import FastAPI
from pydantic import BaseModel
import joblib, pandas as pd, sqlite3
from datetime import datetime

app = FastAPI()
model = joblib.load("aqi_model_24h.pkl")
feats = joblib.load("features.pkl")
DB = "predictions.db"

def init_db():
    con = sqlite3.connect(DB)
    con.execute("""CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TEXT, hour INTEGER, pm2_5 REAL, pm10 REAL,
        aqi_lag1 REAL, aqi_lag24 REAL, predicted_aqi REAL)""")
    con.commit()
    con.close()

init_db()

class Data(BaseModel):
    hour: int
    pm2_5: float
    pm10: float
    aqi_lag1: float
    aqi_lag24: float

@app.post("/predict")
def predict(d: Data):
    X = pd.DataFrame([d.model_dump()])[feats]
    pred = float(model.predict(X)[0])
    con = sqlite3.connect(DB)
    con.execute(
        "INSERT INTO predictions (created_at, hour, pm2_5, pm10, aqi_lag1, aqi_lag24, predicted_aqi) VALUES (?,?,?,?,?,?,?)",
        (datetime.now().isoformat(timespec="seconds"), d.hour, d.pm2_5, d.pm10, d.aqi_lag1, d.aqi_lag24, pred),
    )
    con.commit()
    con.close()
    return {"aqi_24h_later": pred}

@app.get("/history")
def history(limit: int = 20):
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    rows = con.execute("SELECT * FROM predictions ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
    con.close()
    return [dict(r) for r in rows]
