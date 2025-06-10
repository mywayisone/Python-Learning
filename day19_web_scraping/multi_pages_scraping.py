# 💡 Extension (Optional):
# Scrape multiple pages by following the Next button.

# Save quotes to a .txt file.
import requests
from bs4 import BeautifulSoup
import time

url = "https://quotes.toscrape.com"
while True:

    response = requests.get(url)
    # print(response.text)

    parsed_html = BeautifulSoup(response.text, "html.parser")
    quotes = parsed_html.find_all("span", class_="text")
    authors = parsed_html.find_all("small", class_ = "author")

    for quote, author in zip(quotes, authors):
        print(f"{quote.text} - {author.text}")
        filepath = "./day19_web_scraping"
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
