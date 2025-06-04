# 🧩 Mini Project: GitHub Profile Viewer (Console Dashboard)
# You'll combine:

# ✅ requests — to fetch GitHub data
# ✅ prettytable — to format the output
# ✅ colorama — to highlight parts of the interface

# 📄 Create: github_profile_dashboard.py
from colorama import Back, Fore, init, Style
from prettytable import PrettyTable
import requests

# Define the get_user_data() function
def get_user_data():
    try:
        username = input("Enter the username: ")
        url = f"https://api.github.com/users/{username}"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            table = PrettyTable()
            table.field_names = ["Feild", "Value"]
            table.add_row(["Name", data.get("name")])
            table.add_row(["Public Repos", data.get("public_repos")])
            table.add_row(["Followers", data.get("followers")])
            table.add_row(["Following", data.get("following")])
            table.add_row(["Location", data.get("location")])
            table.add_row(["Profile Link", data.get("html_url")])

            print(table)
        else: print("❌ User not found.")
    except requests.exceptions.RequestException as e:
        print("Network error: ", e)


# Define main() function
def main():
    print(Fore.GREEN + "\nGithub Profile\n" + Back.LIGHTBLACK_EX)
    print(Fore.LIGHTGREEN_EX + "=== Github Profile Viewer ===")
    get_user_data()

if __name__ == "__main__":
    main()