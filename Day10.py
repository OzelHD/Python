# 1️⃣ Pick a website that allows scraping (e.g., https://quotes.toscrape.com/).
# 2️⃣ Extract and print all quotes and authors.
# 3️⃣ Handle errors gracefully (e.g., if the request fails).

import requests
from bs4 import BeautifulSoup as BS


url = "https://quotes.toscrape.com/"

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BS(response.text, "html.parser")
    print(f"Title: {soup.title.text}\n")

    quote = soup.find_all("span", class_= "text")
    auth = soup.find_all("small", class_ = "author")
    
    for quotes, authors in zip(quote, auth):
        print(f"{quotes.text} - {authors.text}\n")


except requests.exceptions.RequestException as e:
        print(f"Error fetching quote: {e}")