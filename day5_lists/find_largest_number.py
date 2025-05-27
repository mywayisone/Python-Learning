# 4. Find the largest number in a list
#  - Use a loop or max()

def find_largest_num(list):
    print(max(list))

def find_largest_using_loop(list):
    max = list[0]
    for i in range(1,len(list)):
        if list[i] > max:
            max = list[i]
    print(max)

def main():
    list = [4,2,3,11]
    find_largest_num(list)
    find_largest_using_loop(list)

if __name__ == "__main__":
    main()