# 3. Function that checks if a number is even or odd

number = int(input("Enter number: "))

def even_or_odd(num):
    print("It's Even") if num % 2 == 0 else print("It's Odd")
even_or_odd(number)