import json
import requests
from bs4 import BeautifulSoup
import pathlib

BASE_URL = "https://codingnomads.github.io/recipes/"
page = requests.get(BASE_URL)

# print(page.text)

soup = BeautifulSoup(page.text, features="lxml")
links = soup.find_all("a")

homeingredient= "rice"

links = soup.find_all("a")
link_list = []
joint_links = ""
for link in links:
    joint_links = "https://codingnomads.github.io/recipes/"+ link["href"]
    link_list.append(joint_links)
# print(link_list)

recipes_with_ingredient = []

# print(link_list)
ingredients_list = []

pagex= requests.get(link_list[10])
soupx = BeautifulSoup(pagex.text, features="lxml")
name = soupx.h1.string
body = soupx.find("div", class_="md").find("ul").find_all("li")
for each in body:
    ingredients_list.append(each.text)
print(ingredients_list)

for ingredient in ingredients_list:
    if homeingredient in ingredient.lower():
        recipes_with_ingredient.append(name)


#This doesn't work because not all the links work the same, so I can't scrape all at once. I would have to go one by one. 
# for url in link_list:
    # pagex= requests.get(link_list[10])
    # soupx = BeautifulSoup(pagex.text, features="lxml")
    # name = soupx.h1.string
    # body = soupx.find("div", class_="md").find("ul").find_all("li")
    # for each in body:
    #     ingredients_list.append(each.text)
    # print(ingredients_list)

    # for ingredient in ingredients_list:
    #     if homeingredient in ingredient.lower():
    #         recipes_with_ingredient.append(name)

# print(recipes_with_ingredient)

    #with open(f"python-301-main/04_web-scraping/recipe-scraper/recipe{counter}.html", "wb") as fout:
        #fout.write(page1.content)