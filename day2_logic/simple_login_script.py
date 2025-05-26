# This is a simple login script with hardcoded values

username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "admin123":
    print("Login successfully")
else: print("Access denied!")