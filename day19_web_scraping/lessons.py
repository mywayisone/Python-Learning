# 🕸️ What Is Web Scraping?
# Web scraping is the process of automatically extracting data from websites.

# Think of it like this:

# Just as your browser downloads and displays web pages so you can see them, web scraping downloads pages so a Python script can read and extract specific information.

# 🧠 Why Use Web Scraping?
# You can use it to:
# - Get real-time prices (e.g. from e-commerce sites)
# - Collect job listings, news headlines, or quotes
# - Gather data for analysis when there’s no API
# - Automate repetitive tasks like checking weather or stock updates

# ⚙️ How It Works (Step by Step)
# - Send a request to the website (like opening a page in a browser)
# - Receive HTML in response (the raw page)
# - Parse the HTML using a tool like BeautifulSoup
# - Extract specific content using tag names, classes, or IDs

# 🔍 Example Use Case
# Imagine a site like:
# <div class="quote">
#   <span class="text">"Be yourself; everyone else is already taken."</span>
#   <small class="author">Oscar Wilde</small>
# </div>

# You can write code to grab:
# - The quote from <span class="text">
# - The author from <small class="author">
# That’s web scraping in action!

# 🔍 What You’ll Learn Today

# ✅ Concepts:
# What web scraping is
# - How to inspect and locate HTML elements (via browser DevTools)
# - How to fetch and parse a webpage
# - How to extract specific data from HTML

# 🔧 Tools:
# - requests — fetches webpage content
# - BeautifulSoup — parses HTML

# 🔧 Step 1: Install Required Libraries
# pip install beautifulsoup4
# pip install requests
# ✅ Let me know once that’s done and we’ll jump into writing your first web scraper.


# 🧪 Step 2: Your First Web Scraper
# We’ll scrape the titles of articles from https://quotes.toscrape.com, a practice site made for learning scraping.

# 🔹 Basic Structure
import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the page
url = "https://quotes.toscrape.com"
response = requests.get(url)

# Step 2: Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Find and print all quotes
quotes = soup.find_all("span", class_="text")
for quote in quotes:
    print(quote.text)

# 🧠 What’s Happening?
# - requests.get(url) gets the page.
# - BeautifulSoup(response.text, "html.parser") parses the HTML.
# - soup.find_all(...) searches for specific elements.
# - We loop through each quote and extract the text.

# 📝 Your Practice Task
# 1. Scrape and print:
# - Quote text
# - Author name

# Example Output:
# "Life isn’t about getting and having, it’s about giving and being." - Kevin Kruse

# 💡 Extension (Optional):
# Scrape multiple pages by following the Next button.

# Save quotes to a .txt file.


# 🧩 Up Next:
# Let’s now build on what you've done by exploring:
# - Saving scraped data to a CSV or JSON file
# - Handling missing or broken HTML elements
# - Respecting site rules with robots.txt
# - A 🧠 mini project: Scraping live data from a real public site

# Would you like to:
# - Continue immediately?
# - Or take a break and resume later?


# 🔁 Part 1: Save Scraped Data to a File
# You’ll store the quotes you scraped earlier in a CSV and a JSON file.

# 📝 Save to CSV (quotes.csv)
# Add this to the end of your multi_page.py:

import csv

all_quotes = all_authors = [] #empty list was used to prevent error
with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])  # Header row
    for quote, author in zip(all_quotes, all_authors):
        writer.writerow([quote, author])
# ⚠️ This assumes you’ve stored all quotes and authors in two lists: all_quotes and all_authors.

# 📝 Save to JSON (quotes.json)
import json

data = []
for quote, author in zip(all_quotes, all_authors):
    data.append({"quote": quote, "author": author})

with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

# 🚧 Part 2: Handle Missing Elements Gracefully
# Web pages can be inconsistent. Use .find() carefully:
div ="" # Empty string was used to prevent error
quote_elem = div.find("span", class_="text")
author_elem = div.find("small", class_="author")

quote = quote_elem.text if quote_elem else "N/A"
author = author_elem.text if author_elem else "Unknown"

# 🛡️ Part 3: Be a Responsible Scraper
# 1. Check robots.txt
# Many websites have a file like example.com/robots.txt specifying scraping rules.

# 2. Use delays
# Don’t overload servers. Add a pause between requests:
import time
time.sleep(1)


# 3. Set headers like a browser:
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
requests.get(url, headers=headers)

# 🧪 Your Task
# Update multi_page.py to:

# Save quotes to both quotes.csv and quotes.json

# Gracefully handle missing data
