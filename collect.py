import requests, pandas as pd, os

url = "https://air-quality-api.open-meteo.com/v1/air-quality"
params = {"latitude": 31.5497, "longitude": 74.3436,
          "hourly": "pm10,pm2_5,us_aqi",
          "past_days": 92, "timezone": "Asia/Karachi"}
r = requests.get(url, params=params)
new = pd.DataFrame(r.json()["hourly"])
new["time"] = pd.to_datetime(new["time"])
new = new[new["time"] <= pd.Timestamp.now()]  # forecast hata do

if os.path.exists("lahore_aqi.csv"):
    old = pd.read_csv("lahore_aqi.csv", parse_dates=["time"])
    new = pd.concat([old, new])

new = new.drop_duplicates("time", keep="last").sort_values("time")
new.to_csv("lahore_aqi.csv", index=False)
print("Rows:", len(new))