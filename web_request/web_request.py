import requests
import json

URL = "https://api.escuelajs.co/api/v1/products"

try:
    response = requests.get(url=URL)
    response.raise_for_status()
except requests.HTTPError as exc:
    print(f"An error was encountered {exc}")
else:
    with open("response.json", "w") as file:
        json.dump(response.json(), file, indent=4)