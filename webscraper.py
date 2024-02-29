# Imports
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Currency to convert
to_convert = "EUR"
# Building Url with currency to convert formatted in.
url = f"https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To={to_convert}"

# Getting the page with urlopen method.
page = urlopen(url)

html = page.read()

soup = BeautifulSoup(html, "html.parser")

print(soup.find_all("p")[3].get_text())