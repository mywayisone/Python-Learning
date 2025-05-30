# 5. multiplication_table.py
# - Use nested loop to print 1–12 multiplication table

# Define multiplication_table() function
def multiplication_table():
    for i in range(1, 13):
        for j in range(1, 13):
            print(f"{i} * {j} = {i * j}")
        print("\n")

# Define main() function
def main():
    print("Using nested loop to print multiplication table")
    multiplication_table()

if __name__ == "__main__":
    main()