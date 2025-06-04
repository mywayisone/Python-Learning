# 🧭 Today’s Objectives
# By the end of this lesson, you'll know how to:
# 1. ✅ Install and manage packages using pip
# 2. 📦 Use popular third-party libraries:
#   - colorama – for colored terminal output
#   - requests – for web/API requests
#   - prettytable – for clean table printing
# 3. 📄 Read library documentation and examples
# 4. 💡 Create your own project using at least two of these libraries

# 🔹 Part 1: Installing a Library with pip
# We’ll begin with colorama — a simple library that lets you add color to terminal output.

# ✅ Step-by-Step:
#   => Open your terminal or command prompt
#   => Type: "sudo apt install python3-pip" if you are using Linux/Mac
#   => Use a Virtual Environment (Recommended)
#    - Virtual environments are isolated — safe, easy, and standard practice for Python development.

#    - 💻 Step-by-Step:
#       Inside your day11_external_libraries/ folder, run this:
#       python3 -m venv venv
#       source venv/bin/activate  # (on macOS/Linux)
#              OR
#       venv\Scripts\activate.bat  # (on Windows)
#   => Then install colorama inside the virtual environment:
#      - pip install colorama
# ✅ You're good to go! Run your Python files like normal — colorama will work inside the venv.


# - 🎨 Part 2: Using colorama
# Now let’s create a new file:
# 📄 color_demo.py
from colorama import init, Fore, Back, Style

# Initialize Colorama
init(autoreset=True)

print(Fore.RED + "This is red text.")
print(Fore.GREEN + "This is green text.")
print(Back.YELLOW + "This has a yellow background.")
print(Style.BRIGHT + "This is bright text.")
print(Fore.CYAN + Back.MAGENTA + Style.DIM + "Styled combo text.")

# ✅ init(autoreset=True) ensures color resets automatically after each print.



# 🔹 Next Up: Part 2 — Using the requests Library
# The requests library is one of the most popular Python tools. It lets your program connect to the internet, retrieve data from websites and APIs, and interact with external services.

# 📦 Step 1: Install requests
# In your virtual environment, run: pip install requests
# After successful installation, go to step 2.

# 🌐 Step 2: Using requests to Fetch Data from the Web
# Let’s create a new file:
# 📄 github_user_fetcher.py
# This script will let you enter a GitHub username and fetch their public profile data using GitHub’s API.
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

# 🧪 Try This:
#  - Run the script
#  - Enter your GitHub username or mine: mywayisone
#  - Try a fake username to test the error message