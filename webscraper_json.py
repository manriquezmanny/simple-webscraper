# Imports
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

# Currency to convert
to_convert = "EUR"
# Building Url with currency to convert formatted in.
url = f"https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To={to_convert}"

# Getting the page with urlopen method.
page = urlopen(url)
html = page.read()

#Instanciating soup object.
soup = BeautifulSoup(html, "html.parser")

# Found JSON with all the currencies in an HTML script tag with an id of __NEXT_DATA__. 
# I will parse the JSON out and use the json library to turn it into actual json I can use.
# print(soup.prettify())

# Parsing out just the JSON part of the string.
json_string = soup.find(id="__NEXT_DATA__").get_text()

print(json_string)