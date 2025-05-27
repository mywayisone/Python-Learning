# 2. Add and remove items
#  - Start with a list of 3 fruits
#  - Add 2 more using .append()
#  - Remove one with .remove()

list = ["God", "is", "mine"]

def append(item):
    list.append(item)
    print(list)

def remove(item = ""):
    list.remove(item)
    print(list)

def main():
    append("and")
    append("great")
    append("not")
    remove("not")

if __name__ == "__main__":
    main()