import requests
from bs4 import BeautifulSoup
import time
import random

# Retry function to handle 503 errors with exponential backoff
def request_with_retry(url, headers, retries=3, backoff_factor=1.5):
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 503:
                print(f"503 Error encountered, retrying {attempt + 1}/{retries}...")
                # Wait before retrying (exponential backoff)
                time.sleep(backoff_factor * (2 ** attempt) + random.uniform(0, 1))
            else:
                return response
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}. Retrying {attempt + 1}/{retries}...")
            time.sleep(backoff_factor * (2 ** attempt) + random.uniform(0, 1))
    return None  # Return None if all retries fail


# Function to fetch data from Flipkart
def fetch_flipkart_data(product_name):
    flipkart_data = []
    
    # Construct the search URL for Flipkart laptops
    url = f"https://www.flipkart.com/search?q={product_name.replace(' ', '+')}+laptop"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    r = request_with_retry(url, headers)

    if r and r.status_code == 200:
        soup = BeautifulSoup(r.text, "lxml")
        names = soup.find_all("div", class_="_4rR01T")  # Product names
        prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")  # Product prices

        for name, price in zip(names, prices):
            if product_name.lower() in name.text.lower():  # Filter for exact match
                price_cleaned = price.text.strip().replace('₹', '').replace(',', '')  # Clean the price
                flipkart_data.append({
                    "Product": name.text.strip(),
                    "Price": int(price_cleaned)  # Convert to integer
                })
    else:
        print(f"Failed to retrieve Flipkart data after retries.")
    
    return flipkart_data


# Function to fetch data from Amazon
def fetch_amazon_data(product_name):
    amazon_data = []
    
    # Construct the search URL for Amazon laptops
    url = f"https://www.amazon.in/s?k={product_name.replace(' ', '+')}+laptop"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    r = request_with_retry(url, headers)

    if r and r.status_code == 200:
        soup = BeautifulSoup(r.text, "lxml")
        names = soup.find_all("span", class_="a-size-medium a-color-base a-text-normal")  # Product names
        prices = soup.find_all("span", class_="a-price-whole")  # Product prices

        for name, price in zip(names, prices):
            if product_name.lower() in name.text.lower():  # Filter for exact match
                price_cleaned = price.text.strip().replace(',', '')  # Clean the price
                amazon_data.append({
                    "Product": name.text.strip(),
                    "Price": int(price_cleaned)  # Convert to integer
                })
    else:
        print(f"Failed to retrieve Amazon data after retries.")

    return amazon_data


