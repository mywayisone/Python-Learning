# 📥 Your Turn
# Create a file called settings_manager.py in your day9_csv_json/ folder

# - Paste and modify the code above as needed
# - Run it, test updates, and view the settings.json file
# - Push your work to GitHub

import os
import json

# Default settings
default_settings = {
    "username": "Guest",
    "theme": "light",
    "language": "en"
}

SETTINGS_FILE = "settings.json"

# Define load_settings() function - create the settings.json file
def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "w") as file:
            json.dump(default_settings, file, indent=4)
            view_settings()
    with open(SETTINGS_FILE, "r") as file:
        return json.load(file)

# Define save_setttings() function
def save_settings(settings):
    try:
        with open(SETTINGS_FILE, "w") as file:
            json.dump(settings, file, indent=4)
        view_settings()
    except FileNotFoundError:
        print(f"{SETTINGS_FILE} does not exist in this directory")

# Define update_settings() function - update one setting
def update_setting(key, value):
    try:
        with open(SETTINGS_FILE, "r") as file:
            settings = json.load(file)
            settings[key] = value
            save_settings(settings)
    except FileNotFoundError:
        print(f"{SETTINGS_FILE} does not exist")
        


# Define view_settings() function - display settings
def view_settings():
    try:
        with open(SETTINGS_FILE, "r") as file:
            settings = json.load(file)
            print(settings)
    except FileNotFoundError:
        print(f"{SETTINGS_FILE} not found.")

# Define main() function - Entry point
def main():
    print(load_settings())
    # view_settings()

    key = input("Which setting do you want to change? (username/theme/language): ").strip()
    value = input("New value: ").strip()

    update_setting(key, value)

if __name__ == "__main__":
    main()