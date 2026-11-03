# Lahore Weather & Air Quality Tracker

Fetches live weather and air quality (smog) data for Lahore from the Open-Meteo API, cleans it with Pandas, serves it through a FastAPI app, and visualizes trends.

## What it does
- Fetches hourly temperature, humidity, PM10, PM2.5 and US AQI data
- Converts JSON into Pandas DataFrames
- Plots the 7-day temperature trend and AQI with the 150 "Unhealthy" threshold
- FastAPI endpoints: `/hello` and `/latest` (latest PM2.5 and US AQI)

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
- Compared Linear Regression and Random Forest against a naive baseline (baseline won so far); next: predict 24 hours ahead
