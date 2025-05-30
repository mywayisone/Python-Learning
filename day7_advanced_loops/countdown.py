# 2. countdown.py
# - Print numbers from 10 to 1 using a while loop

counter = 10

# Define counter() function
def countdown(counter: int):
    while counter > 0:
        print(counter)
        counter -= 1

# Define main() function
def main():
    print("\n This program prints from 10-1\n ")
    countdown(counter)


if __name__ == "__main__":
    main()