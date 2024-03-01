### Imports ###
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

# Specify what currencies you'd like to convert to when you want to convert to many currencies here.
convert_to_many = ["EUR", "GBP", "MXN", "CNY", "USD"] 


### FUNCTIONS ###
# Function that converts one currency(first argument) to each currency in convert_to_many(second argument) list.
def one_to_many(convert_from, convert_to_many):
    for currency in convert_to_many:
        # Setting up URL with f-string formatting. Opening URL page. Reading url to get HTML. 
        url = f"https://www.xe.com/currencyconverter/convert/?Amount=1&From={currency}&To={convert_from}"
        page = urlopen(url)
        html = page.read()

        # Instancing a soup object with html and html.parser as arguments.
        soup = BeautifulSoup(html, "html.parser")
        # Scraping each converted currency from list.
        print(soup.find_all("p")[3].get_text())


# Function to convert one currency to another currency.
def one_to_one(convert_from, convert_to):
    # Setting up URL with f-string formatting. Opening URL page. Reading url to get HTML. 
    url = f"https://www.xe.com/currencyconverter/convert/?Amount=1&From={convert_to}&To={convert_from}"
    page = urlopen(url)
    html = page.read()

    # Instancing a soup object with html and html.parser as arguments.
    soup = BeautifulSoup(html, "html.parser")
    # Scraping converted currency.
    scraped_data = soup.find_all("p")[3].get_text()

    # Calling split string method on scraped data. Default delimiter is space.
    scraped_data_split = scraped_data.split()
    # The rate is stored on the 3rd index of the scraped_data_split list.
    # Turning it into a float, rounding it to 2 decimal places, and turning it back into a string.
    rate = str(round(float(scraped_data_split[3]), 2))

    # Formatting the final string I want to print.
    formatted_data = f"1 {scraped_data_split[1]} = {rate} {scraped_data_split[4]}"
    print(formatted_data)


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
            convert_from = input("Enter a valid currency acronym to convert from: ")
        # Calling the one_to_many function I made that converts one currency to many and prints it to terminal.
        one_to_many(convert_from, convert_to_many)


# This is how you do a multi line comment...
"""
The boiler plate code below is so that the main function will only run if this file is the
entry point of my program. In other words, if I import this module to another script, the main 
function will not call and i'll still be able to access the functions I built in that other script.
"""
if __name__ == "__main__":
    main()