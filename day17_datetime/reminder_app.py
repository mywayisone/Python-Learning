# 🌟 Mini Project: Simple Reminder App
# Create a file: reminder_app.py
# Requirements:
# Ask user for a message and time (e.g. 2025-06-04 22:00)
# When the time arrives, print the message
# Optional: Show countdown (every second)
# Use datetime, time.sleep(), and your logic skills here.
from datetime import datetime, timedelta
import time

message = input("Enter the message: ")
msg_time = input("Enter the time: ")

msg_time = datetime.strptime(msg_time, "%Y-%m-%d  %H:%M") # Converts the input string to datetime
future_time_in_sec = int((msg_time - datetime.now()).total_seconds()) # Converts datetime to seconds to int
for sec in range(future_time_in_sec, 0, -1): # Decrement sec as it loops
    print(f"{timedelta(seconds=sec)} remaining...", end="\r") # Converts sec to time format for each loop
    time.sleep(1) # sleep for 1 sec
print("\n",message)
