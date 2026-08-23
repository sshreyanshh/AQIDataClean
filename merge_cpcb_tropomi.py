import pandas as pd

cpcb = pd.read_csv("data/processed/anand_vihar_daily.csv")
cpcb["date"] = pd.to_datetime(cpcb["Timestamp"]).dt.tz_localize(None).dt.normalize()
cpcb = cpcb.drop(columns=["Timestamp"])

sat = pd.read_csv("data/processed/tropomi_daily_clean.csv")
sat["date"] = pd.to_datetime(sat["date"])

merged = pd.merge(cpcb, sat, on="date", how="left")
merged = merged.sort_values("date").reset_index(drop=True)

merged.to_csv("data/processed/cpcb_tropomi_daily.csv", index=False)

print(merged.shape)
print(merged.isna().mean() * 100)
print(merged.head())