import requests

# In three lines of code, fetch the HTML text from CodingNomads'
# main page and print it to your console.
#
# If you run into encoding/decoding errors, you're experiencing something
# very common. head over to StackOverflow and find a solution!

URL = ("https://platform.codingnomads.co/learn/my/")
page = requests.get(URL)
print(page.text)
