# Lahore Weather & Air Quality Tracker

Fetches live weather and air quality (smog) data for Lahore from the Open-Meteo API, cleans it with Pandas, stores it in SQLite, predicts AQI 24 hours ahead with scikit-learn, and serves the model through FastAPI.

## What it does
- Fetches hourly temperature, humidity, PM10, PM2.5 and US AQI data
- Converts JSON into Pandas DataFrames and plots trends
- Stores data in SQLite and analyses it with SQL
- FastAPI endpoints: `/hello`, `/latest` and `/predict` (POST)

## SQL analysis
Hourly AQI data for Lahore (about 840 hours) was stored in SQLite (`aqi.db`).

- Worst day: 2 Nov 2026 (average US AQI 205, peak 215)
- Unhealthy hours: 577 of about 840 hours (roughly 69%) had AQI above 150
- Worst time of day: around 6 PM (average AQI 164) and early morning (5-6 AM)

Queries used: `GROUP BY`, `AVG`, `MAX`, `COUNT`, `ORDER BY ... LIMIT`.
Note: the data includes some forecast hours, so exact numbers may change when the notebook is re-run.

## Model results (24 hours ahead)
On about 3 months of hourly data, Linear Regression (MAE 13.3) beat the "same as now" baseline (MAE 14.2), but only by a small margin. Random Forest (MAE 15.3) did not beat the baseline.

## Limitations
- Only about 3 months of data, so results are early
- The model is pulled towards the average AQI

## Tech
Python, Requests, Pandas, Matplotlib, scikit-learn, SQLite, FastAPI, Uvicorn, Google Colab

## Run the API
```
pip install fastapi uvicorn requests scikit-learn joblib pandas
uvicorn main:app --reload
```
Then open `http://127.0.0.1:8000/docs`

## Next steps
- Collect data daily to build my own dataset
- Add a `/history` endpoint
- Improve the model with more lag features
