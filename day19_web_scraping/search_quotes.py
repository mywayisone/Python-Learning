# 🧠 Mini Project: Top Quotes Explorer
# 🎯 Objective
# Scrape all quotes and authors from https://quotes.toscrape.com, save them to a file, and allow a user to search for quotes by author.

import json

# Define the search() function
def search(author):
    try:
        filepath = "./day19_web_scraping"
        with open(f"{filepath}/multi_page.json", "r") as file:
            quotes = json.load(file)
    except FileNotFoundError as e:
        print(f"Error occured: {e}")
    else:
        for key, quote in quotes.items():
            if author in quote["author"]:
                print(f"{quote["text"]} - {quote["author"]}")
                return
        print("Author does not exist")  

def main():
    userinput = input("Enter the author's name: ")
    search(userinput)

if __name__ == "__main__":
    main()