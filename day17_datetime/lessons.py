# 📅 Day 17: Working with Dates & Time in Python
# This is super important for:
# - Logging and reporting
# - Scheduling apps
# - Calculating time differences
# - Handling timestamps from APIs, databases, and file systems


# 🔍 What You'll Learn Today:
# 1. Using datetime module
# 2. Working with:
#   - date
#   - time
#   - datetime
#   - timedelta
# 3. Formatting and parsing date strings (strftime, strptime)
# 4. Time arithmetic (e.g., “7 days ago”, “2 hours later”)
# 5. Real-world use cases
# 6. 📝 Practice Tasks
# 7. 🌟 Mini Project: Simple Reminder App

# 🕒 1. Using the datetime Module
import datetime

# 📅 2. Working with date
from datetime import date

today = date.today()
print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

# Creating a specific date
birthday = date(1995, 5, 14)
print("Birthday:", birthday)

# ⏰ 3. Working with time
from datetime import time

t = time(14, 30, 15)
print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)

# 📆 4. Working with datetime
from datetime import datetime

now = datetime.now()
print("Now:", now)

# Custom datetime
custom_dt = datetime(2025, 6, 4, 9, 0)
print("Custom datetime:", custom_dt)


# ➕ 5. Working with timedelta
from datetime import timedelta

# 7 days from now
seven_days = timedelta(days=7)
future_date = datetime.now() + seven_days
print("7 Days Later:", future_date)

# Time difference
delta = datetime(2025, 6, 11) - datetime.now()
print("Days till June 11:", delta.days)

# 🧪 6. Formatting and Parsing Dates
# Formatting with strftime
print("Formatted:", now.strftime("%Y-%m-%d %H:%M:%S"))

# Parsing string with strptime
date_str = "2025-06-04 08:00"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
print("Parsed datetime:", parsed_date)


# 🔄 7. Real-World Use Cases (Quick Examples)
# Logging timestamp
# Countdown till an event
# Reminders
# Date validation in forms

# ✍️ Practice Tasks
# Print today’s date in this format: Wednesday, 04 June 2025
# Print the number of days between your birthday and today
# Calculate the time 2 hours and 30 minutes from now
# Parse this string: "14/02/2025 15:45" using strptime

# 🌟 Mini Project: Simple Reminder App
# Create a file: reminder_app.py
# Requirements:
# Ask user for a message and time (e.g. 2025-06-04 22:00)
# When the time arrives, print the message
# Optional: Show countdown (every second)
# Use datetime, time.sleep(), and your logic skills here.