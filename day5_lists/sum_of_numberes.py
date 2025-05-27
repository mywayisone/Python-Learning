# 3. Sum a list of numbers
# numbers = [5, 10, 20, 7]
# Calculate total sum

def sum_list(list):
    print(sum(list))

def sum_using_forloop(list):
    sum = 0
    for item in list:
        sum += item
    print(sum)

def main():
    num_list = [5,6,7,8,9]
    sum_list(num_list)
    sum_using_forloop(num_list)

if __name__ == "__main__":
    main()