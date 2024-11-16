import requests
from bs4 import BeautifulSoup
import csv

# URL of the website to scrape
url = 'https://www.amazon.in/realme-TechLife-Headphone-Playtime-ANC-Black/dp/B0DJFHBQH2/ref=sr_1_11?crid=62NQ2LOV5UGP&dib=eyJ2IjoiMSJ9.jPvfZB3uAQaO1nLnMldKqoVfoVcFYimt-GitdeMk3hSKlYNHbMTOpvLXtgCr-uI6SW2hlOfj1fZuavpnR4Gd10ntYx7PlUGtQmMJwjWQ1NYB8Ja3MEVNhzhC-L0k5hzZE58r2DMddCyMQYNCpm0DcV0Tj2zqAdQlP8H4a1uAl2gUwyK3CUR8iqBf-786edHWPsqREcays0Y8Hu6bxwF_FOCDNYS_kSmfr11mLR-zLxIlPCTe0TeIAqeeUpESCa5O7Vrcw2wxxG4wv9rA4PtF1hZbPINp9XyO-8gH_nVLxd4.k5LYkcD4JqhqyL7tMjQa6VJjkuv6PJOei9a8hg4NONo&dib_tag=se&keywords=realme%2Bheadphones&nsdOptOutParam=true&qid=1731677328&s=electronics&sprefix=realme%2Bhe%2Celectronics%2C290&sr=1-11&th=1'

# Set headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Make a request to the website
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all products on the page
    products = soup.find_all('div', class_='product')  # Adjust class based on website structure

    # Create a CSV file to store the scraped data
    with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Product Name', 'Price', 'Rating'])

        # Loop through each product and extract the desired data
        for product in products:
            # Extract product name
            name = product.find('h2', class_='product-name').text.strip()

            # Extract product price
            price = product.find('span', class_='price').text.strip()

            # Extract product rating (if available)
            rating_tag = product.find('div', class_='rating')
            rating = rating_tag.text.strip() if rating_tag else "No rating"

            # Write data to CSV
            writer.writerow([name, price, rating])

    print("Data has been successfully scraped and saved to 'products.csv'.")

else:
    print(f"Failed to retrieve the website. Status code: {response.status_code}")
