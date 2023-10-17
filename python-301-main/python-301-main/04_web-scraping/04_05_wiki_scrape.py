import requests
from bs4 import BeautifulSoup

# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

BASE_URL = "https://en.wikipedia.org/wiki/Web_scraping"
page = requests.get(BASE_URL)

# print(page.text)

soup = BeautifulSoup(page.text, features="html.parser")

links = soup.find_all("a")


links = soup.find_all("a")
link_list = []

# for link in links:
#     if link["href"].startswith("/wiki"):
#         print(link["href"])
    
# print(link_list)
link_list = []
body = soup.find("div", class_="mw-parser-output").find_all("a")
for link in body:
    if link["href"].startswith("/wiki"):
        link_list.append(link["href"])

basewikilink =  "https://en.wikipedia.org"
newlink = basewikilink + link_list[21]
print(newlink)
newpage = requests.get(newlink)
soup2 = BeautifulSoup(newpage.text, features="html.parser")
body2 = soup2.find("div", id="bodyContent").text
# print(body2)
with open("python-301-main/04_web-scraping/wikicontent", "w") as fout:
    fout.write(body2)