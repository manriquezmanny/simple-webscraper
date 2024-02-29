# Imports
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

# Currency to convert
toConvert = "GBP"
# Building Url with currency to convert formatted in.
url = f"https://www.xe.com/currencyconverter/"

# Getting the page with urlopen method.
page = urlopen(url)

html = page.read()

soup = BeautifulSoup(html, "html.parser")

# Found JSON with all the currencies in an HTML script tag with an id of __NEXT_DATA__. I will parse the JSON out and use that.
# print(soup.prettify())

json_string = soup.find(id="__NEXT_DATA__").get_text()

print(json_string)