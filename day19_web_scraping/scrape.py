# 📝 Your Practice Task
# 1. Scrape and print:
# - Quote text
# - Author name

# 2. Example Output:
# "Life isn’t about getting and having, it’s about giving and being." - Kevin Kruse

# Save quotes to a .txt file.

import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
response = requests.get(url)

parsed_html = BeautifulSoup(response.text, "html.parser")
# print(parsed_html) - inspection

quotes = parsed_html.find_all("span", class_= "text")
# print(quotes) - for inspection

authors = parsed_html.find_all("small", class_ = "author")
# print(authors)- for inspection

for quote, author in zip(quotes, authors):
    print(f"{quote.text} - {author.text}")
    filepath = "./day19_web_scraping" # depending on the directory you are running the script
    with open(f"{filepath}/single_page.txt", "a") as file:
        file.write(f"{quote.text} - {author.text}\n")
