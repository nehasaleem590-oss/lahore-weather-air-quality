# Lahore Weather & Air Quality Tracker

Fetches live weather and air quality (smog) data for Lahore from the Open-Meteo API, cleans it with Pandas, serves it through a FastAPI app, and visualizes trends.

## What it does
- Fetches hourly temperature, humidity, PM10, PM2.5 and US AQI data
- Converts JSON into Pandas DataFrames
- Plots the 7-day temperature trend and AQI with the 150 "Unhealthy" threshold
- FastAPI endpoints: `/hello` and `/latest` (latest PM2.5 and US AQI)
- - `/predict` (POST): predicts AQI 24 hours ahead from hour, PM2.5, PM10, and AQI lags
- Linear Regression (MAE 15.9) beat the "same as now" baseline (MAE 22.9) on ~7 days of held-out data

## Limitations
- Only ~30 days of data, so results are early
- Model tends to pull predictions toward the 30-day average

## Tech
Python, Requests, Pandas, Matplotlib, FastAPI, Uvicorn, Google Colab

## Files
- `lahore_weather_analysis (1).ipynb`: data fetching, cleaning and charts
- `main.py`: FastAPI app

## Run the API
pip install fastapi uvicorn requests
uvicorn main:app --reload

## Next steps
- Store data in SQL (SQLite)
- ## SQL Analysis

Hourly AQI data for Lahore was stored in a SQLite database (`aqi.db`) and analysed with SQL queries.

**Key findings:**
- **Worst days:** early November, with daily average US AQI around 200
- **Unhealthy hours:** about two-thirds of all hours had AQI above 150
- **Worst time of day:** 5 PM to 8 PM, peaking around 6 PM

**Queries used:** `GROUP BY` on day and hour, `AVG`, `MAX`, `COUNT`, `ORDER BY ... LIMIT`.

**Note:** The dataset includes forecast hours, so exact numbers may change when the notebook is re-run.
- Compared Linear Regression and Random Forest against a naive baseline (baseline won so far); next: predict 24 hours ahead
- ## SQL Analysis

Hourly AQI data for Lahore (~840 hours) was stored in a SQLite database (`aqi.db`) and analysed with SQL queries.

**Key findings:**
- **Worst day:** 2 Nov 2026 (average US AQI 205, peak 215)
- **Unhealthy hours:** 554 of ~840 hours (about 66%) had AQI above 150
- **Worst time of day:** 5 PM to 8 PM, peaking at 6 PM (average AQI 162)

**Queries used:** `GROUP BY` on day and hour, `AVG`, `MAX`, `COUNT`, `ORDER BY ... LIMIT`.
**Note:** The dataset includes forecast hours, so exact numbers may change when the notebook is re-run.
