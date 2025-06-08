# ✍️ Practice Tasks
# Print today’s date in this format: Wednesday, 04 June 2025
# Print the number of days between your birthday and today
# Calculate the time 2 hours and 30 minutes from now
# Parse this string: "14/02/2025 15:45" using strptime
from datetime import date, time, timedelta, datetime

# 1. Print today’s date in this format: Wednesday, 04 June 2025
today = datetime.today()
print(today.strftime("%A, %d %B %Y"))

# In this code:
# - %A formats the day of the week as a full name (e.g., Monday, Tuesday, etc.)
# - %B formats the month as a full name (e.g., January, February, etc.)
# - %d formats the day of the month as a zero-padded decimal
# - %Y formats the year as a four-digit decimal

# 2. Print the number of days between your birthday and today
birthday = date(1993, 11, 20)
difference = date.today() - birthday
print(difference)

# 3. Calculate the time 2 hours and 30 minutes from now
two_hours_half = timedelta(hours=2, minutes=30)
future = datetime.now() + two_hours_half
print(future)

# 4. Parse this string: "14/02/2025 15:45" using strptime
date_str = "14/02/2025 15:45"
parsed_date = datetime.strptime(date_str, "%d/%m/%Y  %H:%M")
print(parsed_date)