# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

import requests
from bs4 import BeautifulSoup

url = "https://iufost.org/"
page = requests.get(url)
soup = BeautifulSoup(page.text, features="html.parser").prettify("utf-8")

with open ("python-301-main/04_web-scraping/iufost.html", "wb") as fout:
    fout.write(page.content)