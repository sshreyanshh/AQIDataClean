import requests

STATIONS = {
    "anand_vihar": "https://data.opencity.in/dataset/0dc7b9fe-9fd4-46ee-a37e-88f0bd6f6362/resource/5ef3f66f-2bb0-4593-91db-ba6e693a77f3/download/del-anand-vihar-dpcc-2024-25.csv",
    "rk_puram": "https://data.opencity.in/dataset/0dc7b9fe-9fd4-46ee-a37e-88f0bd6f6362/resource/d9dfd28d-038d-448f-8e33-5e6f6b32d15c/download/del-r-k-puram-dpcc-2024-25.csv",
    "punjabi_bagh": "https://data.opencity.in/dataset/0dc7b9fe-9fd4-46ee-a37e-88f0bd6f6362/resource/82080ddc-e094-4a3a-8421-242ec6bc8a45/download/del-punjabi-bagh-dpcc-2024-25.csv",
    "mandir_marg": "https://data.opencity.in/dataset/0dc7b9fe-9fd4-46ee-a37e-88f0bd6f6362/resource/922c72d8-c66e-4336-8cd9-49898776ca69/download/del-mandir-marg-dpcc-2024-25.csv",
    "rohini": "https://data.opencity.in/dataset/0dc7b9fe-9fd4-46ee-a37e-88f0bd6f6362/resource/f6be929b-151a-4b92-b5b4-507481b15128/download/del-rohini-dpcc-2024-25.csv",
}

for name, url in STATIONS.items():
    print(f"Downloading {name}.")
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    with open(f"data/raw/{name}.csv", "wb") as f:
        f.write(response.content)
    print(f"  saved data/raw/{name}.csv ({len(response.content)/1e6:.1f} MB)")

print("Done.")