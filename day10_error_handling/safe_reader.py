filename = input("Enter a file name to open: ")

try:
    with open(filename, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("That file does not exist.")
except Exception as e:
    print("Something went wrong:", e)
else:
    print("File read successfully.")
finally:
    print("End of script.")
