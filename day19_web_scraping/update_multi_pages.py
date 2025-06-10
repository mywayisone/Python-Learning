# 💡 Extension (Optional):
# Scrape multiple pages by following the Next button.

# Save quotes to a .txt file.

# 🧪 Your Task
# Update multi_page.py to:
# - Save quotes to both quotes.csv and quotes.json
# - Gracefully handle missing data

import requests
from bs4 import BeautifulSoup
import time
import json
import csv

# def save_as_json(text, author):
#     filepath = "./day19_web_scraping"
#     with open(f"{filepath}/multi_page.json", "r") as file:
#         quotes = json.load(file)
#         key = len(quotes) + 1
#         quotes[key] = {"author" : author, "text" : text}

url = "https://quotes.toscrape.com"
csv_file = []
json_file = {}
filepath = "./day19_web_scraping"

while True:

    response = requests.get(url)
    # print(response.text)

    parsed_html = BeautifulSoup(response.text, "html.parser")
    quotes = parsed_html.find_all("span", class_="text")
    authors = parsed_html.find_all("small", class_ = "author")

    for quote, author in zip(quotes, authors):
        print(f"{quote.text} - {author.text}")
        key = len(json_file) + 1
        json_file.update({key : {"author": author.text, "text": quote.text}})
        csv_file.append({"author": author.text, "text": quote.text})

        with open(f"{filepath}/multi_page.txt", "a") as file:
            file.write(f"{quote.text} - {author.text}\n")

    next_page = parsed_html.find("li", class_="next")    
    if next_page:
        next_page = parsed_html.find("li", class_="next").find("a")
        next_page_url = next_page['href']
        print(next_page_url)

        url = f"https://quotes.toscrape.com{next_page_url}"
        time.sleep(1)
    else:
        break

if len(json_file):
    with open(f"{filepath}/multi_page.json", "a") as file:
        json.dump(json_file, file, indent=4 )

if len(csv_file):
    with open(f"{filepath}/multi_page.csv", "a", newline="") as file:
        fieldnames = ["author", "text"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if file.tell() == 0:
            writer.writeheader()
        writer.writerows(csv_file)


    