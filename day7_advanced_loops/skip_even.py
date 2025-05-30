# 3. skip_even.py
# - Loop 1–20, print only odd numbers using continue

# Define skip_even() function
def skip_even():
    for i in range(1, 21):
        if i % 2 == 0:
            continue
        print(i)

# Define main() function 
def main():
    print("\n This progam skips even number between 1-20")
    skip_even()

if __name__ == "__main__":
    main()
