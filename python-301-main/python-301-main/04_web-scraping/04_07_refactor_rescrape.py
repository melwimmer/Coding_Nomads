# Refactor your web scraping script and wrap all the functionality into
# separate functions. This is a great exercise to revisit writing functions
# as well as for refactoring your code. It'll also help you in an upcoming
# section of the course when you'll write tests for your web scraper.
import requests
from bs4 import BeautifulSoup
import json

# def saving_html_request(url, saving_path):
#     page = requests.get(url)
    

#     with open (saving_path, "wb") as fout:
#         fout.write(page.content)

# to open the file and use it I can use:
def printing_whole_soup(path):
    with open(path, 'rb') as f:
        soup = BeautifulSoup(f.read())
        print(soup)

# def opening_html(saved_path):
#     with open (saved_path, "r") as fin:
#         page = fin.read

# def saving_json_request(url, saving_path):
#     response = requests.get(url)
#     data = response.json()

#     with open(saving_path, "w") as fout:
#         json.dump(data, fout)

# def opening_the_json(opening_path):
#     with open(opening_path, "r") as fin:
#         data1 = json.load(fin)


        