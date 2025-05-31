# 1. write_greeting.py
# - Ask user for their name
# - Write: "Hello, [name]!" to a file

# Define greeting() function
def greeting(name: str):
    with open("greeting.txt", "w") as file:
        file.write(f"Hello, {name}! I'm sure you are faring well in the presence of God. \nKeep radiating in His grace, pal.")

# Define main() function 
def main():
    name = input("Enter your name: ")
    greeting(name)


if __name__ == "__main__":
    main()