import requests
from prettytable import PrettyTable

username = input("Enter a GitHub username: ")
url = f"https://api.github.com/users/{username}"

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        table = PrettyTable()
        table.field_names = ["Field", "Value"]
        table.add_row(["Name", data.get("name")])
        table.add_row(["Public Repos", data.get("public_repos")])
        table.add_row(["Followers", data.get("followers")])
        table.add_row(["Following", data.get("following")])
        table.add_row(["Location", data.get("location")])
        table.add_row(["Profile URL", data.get("html_url")])

        print(table)
    else:
        print("❌ User not found.")
except requests.exceptions.RequestException as e:
    print("⚠️ Network error:", e)