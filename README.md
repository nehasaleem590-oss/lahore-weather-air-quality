# Lahore Weather & Air Quality Tracker

Fetches live weather and air quality (smog) data for Lahore from the Open-Meteo API, cleans it with Pandas, and visualizes trends.

## What it does
- Fetches hourly temperature and humidity data
- Fetches PM10, PM2.5 and US AQI data
- Converts JSON into Pandas DataFrames
- Plots the 7-day temperature trend and AQI with the 150 "Unhealthy" threshold

## Tech
Python, Requests, Pandas, Matplotlib, Google Colab

## Notebook
`lahore_weather_analysis (1).ipynb`

## Next steps
- FastAPI endpoints for latest and historical data
- ML model to predict air quality
- Flutter app to show predictions
