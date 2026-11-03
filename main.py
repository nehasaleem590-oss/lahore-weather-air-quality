import requests
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def hello():
    return {"message": "Hello Neha"}


@app.get("/latest")
def latest():
    url = "https://air-quality-api.open-meteo.com/v1/air-quality"
    params = {
        "latitude": 31.5497,
        "longitude": 74.3436,
        "hourly": "pm2_5,us_aqi",
        "timezone": "Asia/Karachi",
    }
    r = requests.get(url, params=params)
    data = r.json()["hourly"]
    return {
        "time": data["time"][0],
        "pm2_5": data["pm2_5"][0],
        "us_aqi": data["us_aqi"][0],
    }