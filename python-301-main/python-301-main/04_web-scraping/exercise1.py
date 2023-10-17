import json
import requests

response = requests.get("https://ghibliapi-iansedano.vercel.app/api/films")
data = response.json()

with open("python-301-main/04_web-scraping/films.json", "w") as fout:
    json.dump(data, fout)