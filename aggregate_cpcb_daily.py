import pandas as pd

df = pd.read_csv("data/processed/anand_vihar_hourly.csv", parse_dates=["Timestamp"], index_col="Timestamp")

numeric_cols = ["pm25", "pm10", "no2", "so2", "co", "ozone", "temp", "humidity", "wind_speed", "wind_dir"]

daily_mean = df[numeric_cols].resample("D").mean()
daily_count = df[numeric_cols].resample("D").count()

MIN_HOURS = 16

for col in numeric_cols:
    daily_mean.loc[daily_count[col] < MIN_HOURS, col] = pd.NA

daily_mean.to_csv("data/processed/anand_vihar_daily.csv")

print(daily_mean.shape)
print(daily_mean.isna().mean() * 100)
print(daily_mean.head())