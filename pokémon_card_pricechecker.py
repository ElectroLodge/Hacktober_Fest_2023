import requests
from bs4 import BeautifulSoup
import pandas as pd

# Get info from user
card = input("Card Name (Ex: Pikachu): ");
set = input("Set Name (Ex: Evolving Skies): ");
card_number = input("Card number (Ex: 51): ");

# Build the urls for scrapping
url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw='+card+'+'+set+'+'+card_number+'%2F108&_sacat=0&Graded=No&_dcat=183454&LH_Auction=1&rt=nc&LH_Sold=1&LH_Complete=1'

grade10_url = 'https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&LH_Auction=1&LH_Sold=1&LH_Complete=1&_nkw='+card+'+'+set+'+'+card_number+'%2F108&Graded=Yes&_oaa=1&_fsrp=1&rt=nc&Grade=10&_dcat=183454'

grade9_url = 'https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&LH_Auction=1&LH_Sold=1&LH_Complete=1&_nkw='+card+'+'+set+'+'+card_number+'%2F108&Graded=Yes&_oaa=1&_fsrp=1&rt=nc&Grade=9&_dcat=183454'

# Scrape the url and get data
def getData(url):
  r = requests.get(url)
  soup = BeautifulSoup(r.text, 'html.parser')
  return soup

def parse(soup):
  found_results = soup.find_all('div', {'class': 'srp-save-null-search'}) == []
  prices = []

  # Check if card exists
  if (found_results):
    # If it does, scrape data to get price
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    for item in results:
      prices.append(float(item.find('span', {'class': 's-item__price'}).text.replace("$", "").strip()))
  else: 
    # Tell user unable to find card if card doesn't exist
    print()
    print("Unable to find the card, please try again.")
    print("\nInfo from: " + url)
    quit()

  # Return average price
  return round(sum(prices) / len(prices))
  

ungraded_Data = getData(url)
grade10_Data = getData(grade10_url)
grade9_Data = getData(grade9_url)

ungraded_price = parse(ungraded_Data)
grade10_price = parse(grade10_Data)
grade9_price = parse(grade9_Data)

# Give user the price results
print()
print()
print("Prices:")
print("----------")
print("Ungraded: $" + str(ungraded_price))
print("Grade 10: $" + str(grade10_price))
print("Grade 9: " + str(grade9_price))
print()
print("Info from: " + url)
