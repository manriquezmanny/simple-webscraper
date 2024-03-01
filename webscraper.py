""" Website I am Scraping: xe.com """

### Imports ###
import math as Math
from bs4 import BeautifulSoup
from urllib.request import urlopen

### GLOBAL VARIABLES ###
# Added valid currencies i'd like this app to be able to check. If anyone clones this repository, feel free to add any I missed.
# Chose to use a dictionary/object here so that checking for valid currency is constant time instead of linear if I had to iterate over list/array.
currencies = { 
                "AUD": True, "EUR": True, "JPY": True, "USD": True, "CHF": True,
                "CNY": True, "CUP": True, "DOP": True, "EGP": True, "GBP": True,
                "MXN": True, "NZD": True, "RUB": True, "KRW": True, "RON": True   
             }
"""
Specify what currencies you'd like to convert to, when you want to convert to many currencies,
in the convert_to_many variable below. It is currently set to all key values in currencies variable above.
You can set the convert_to_many variable to a list/array of only the currencies you want to convert if you want. 
Make sure Each acronym in the list/array is a valid acronym with all letters uppercased.
"""
convert_to_many = currencies.keys()


### FUNCTIONS ###
# Function that converts one currency(first argument) to each currency in convert_to_many(second argument) list.
def one_to_many(convert_from, convert_to_many):
    for currency in convert_to_many:
        # Setting up URL with f-string formatting. Opening URL page. Reading url to get HTML. 
        url = f"https://www.xe.com/currencyconverter/convert/?Amount=1&From={currency}&To={convert_from}"
        # Getting Scraped data with my scraped_data function.
        scraped_data = scrape_data(url)
        # Formatting data with my format_data function and printing it.
        formatted_data = format_data(scraped_data)
        print(formatted_data)


# Function to convert one currency to another currency.
def one_to_one(convert_from, convert_to):
    # Setting up URL with f-string formatting. Opening URL page. Reading url to get HTML. 
    url = f"https://www.xe.com/currencyconverter/convert/?Amount=1&From={convert_to}&To={convert_from}"
    # Getting scraped data with my scrape_data function.
    scraped_data = scrape_data(url)

    # Formatting scraped data with my format_data function and printing it.
    formatted_data = format_data(scraped_data)
    print(formatted_data)


# Function to format conversion to print.
def format_data(string):
    # Splitting the unrounded string by the default space delimiter.
    str_list = string.split()
    # Getting rid of commas so that float() function doesn't fail on next line.
    str_list[3] = str(str_list[3]).replace(",", "")
    # Getting just the rate, turning it into a float, rounding it, and turning back into a string.
    rate = str(round(float(str_list[3]), 2))
    # Setting up my formatted string just how I want it with an f-string.
    formatted_str = f"1 {str_list[1]} = {rate} {str_list[4]}"
    # Returning formatted string.
    return formatted_str


# Function to scrape the data I need.
def scrape_data(url):
    # Opening url
    page = urlopen(url)
    # Reading oppened url.
    html = page.read()

    # Instancing a soup object with html string from url and html.parser as arguments.
    soup = BeautifulSoup(html, "html.parser")
    # Getting the converted currency from p tag in HTML.
    scraped_data = soup.find_all("p")[3].get_text()
    # Returns scraped data.
    return scraped_data


### MAIN FUNCTION ###
# Main function that handles asking user for input and running functions accordingly.
def main():
    # Will use to ensure valid input.
    invalid_input = True

    # Asking for valid input until valid input given.
    while invalid_input:
        user_input = input('\nWould you like to:\n"A" Convert one currency to another?\n"B" Convert one currency to many?\nEnter "A" or "B": ')
        user_input = user_input.lower().strip()

        # Ternary to check if valid input was given.
        invalid_input = False if user_input == "a" or user_input == "b" else True 
    
    # If user input is a, getting necessary user input and converting one currency to another.
    if user_input == "a":
        # Creating two variables i'll use to handle getting valid user input.
        convert_from = "invalid"
        convert_to = "invalid"

        # Asking for valid input until valid currency entered. keys() method returns list/array of key values from currencies dictionary/object.
        while convert_from not in currencies.keys():
            convert_from = input("\nEnter a valid currency acronym to convert from: ").upper()
        # Asking for valid input until valid currency entered again.    
        while convert_to not in currencies.keys():
            convert_to = input("Enter a valid currency acronym to convert to: ").upper()

        # Calling the one to one function I made that prints the result of converting one currency to another. 
        one_to_one(convert_from, convert_to)

    # Else user input was b, so getting necessary user input and converting one currency to many others.
    else:
        # Creating falsy variable that will be updated to handle user input.
        convert_from = "invalid"
        # Asking for input until valid input recieved. Currencies.keys() returns key values from currencies dictionary/object.
        while convert_from not in currencies.keys():
            convert_from = input("\nEnter a valid currency acronym to convert from: ").upper()
        # Calling the one_to_many function I made that converts one currency to many and prints it to terminal.
        one_to_many(convert_from, convert_to_many)

"""
The boiler plate code below is so that the main function will only run if this file is the
entry point of my program. In other words, if I import this module to another script, the main 
function will not call and i'll still be able to access the functions I built in that other script.
"""
if __name__ == "__main__":
    main()