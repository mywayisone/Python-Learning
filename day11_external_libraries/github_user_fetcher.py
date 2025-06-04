import requests

username = input("Enter a GitHub username: ")
url = f"https://api.github.com/users/{username}"

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Name: {data.get('name')}")
        print(f"Public Repos: {data.get('public_repos')}")
        print(f"Followers: {data.get('followers')}")
        print(f"Profile URL: {data.get('html_url')}")
    else:
        print("User not found.")
except requests.exceptions.RequestException as e:
    print("Network error:", e)
