import pandas as pd

no2 = pd.read_csv("data/raw/Anand_Vihar_TROPOMI_NO2_2024_2025.csv")
co = pd.read_csv("data/raw/Anand_Vihar_TROPOMI_CO_2024_2025.csv")

no2["date"] = pd.to_datetime(no2["date"])
co["date"] = pd.to_datetime(co["date"])

no2 = no2.drop_duplicates(subset=["date"], keep="first")
co = co.drop_duplicates(subset=["date"], keep="first")

no2 = no2[["date", "NO2"]].rename(columns={"NO2": "no2_trop"})
co = co[["date", "CO"]].rename(columns={"CO": "co_trop"})

sat = pd.merge(no2, co, on="date", how="outer").sort_values("date").reset_index(drop=True)

full_range = pd.DataFrame({"date": pd.date_range(sat["date"].min(), sat["date"].max(), freq="D")})
sat = pd.merge(full_range, sat, on="date", how="left")

sat.to_csv("data/processed/tropomi_daily_clean.csv", index=False)

print(sat.shape)
print(sat.isna().mean() * 100)
print(sat.head())