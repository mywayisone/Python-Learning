import logging

# Set up logging
logging.basicConfig(filename="errors.log", level=logging.ERROR)

try:
    num = int(input("Enter a number: "))
    print(10 / num)
except Exception as e:
    logging.error("An error occurred: %s", e)
    print("Something went wrong. Error logged.")

