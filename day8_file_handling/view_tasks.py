# view_tasks.py
# - Show all tasks in todo.txt

# Define view_tasks.py function
def view_tasks():
    try:
        filename = "todo.txt"
        with open(filename, "r") as file:
            contents = file.readlines()
            if contents:
                for index, content in enumerate(contents):
                    print(f"{index}. {content}")
            else: print(f"{filename} is empty")
    except FileNotFoundError:
        print(f"{filename} does not exist in this directory")

# Define the main() function
def main():
    view_tasks()

if __name__ == "__main__":
    main()