# Imports
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Currency to convert
to_convert = ["EUR", "GBP", "MXN", "CNY"]

for currency in to_convert:
    # URL passing current currency in loop.
    url = f"https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To={currency}"
    # Opening url with urlopen method.
    page = urlopen(url)
    # Reading the HTML DOM and storing it in html.
    html = page.read()
    # Instancing a soup object with our html DOM and html.parser as arguments.
    soup = BeautifulSoup(html, "html.parser")
    # Scraping each converted currency from list.
    print(soup.find_all("p")[3].get_text())