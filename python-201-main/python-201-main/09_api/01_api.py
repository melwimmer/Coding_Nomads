import requests

min_len = 2
max_len = 7

url = f"https://uzby.com/api.php?min={min_len}&max={max_len}"

response = requests.get(url)
print(response.text)

