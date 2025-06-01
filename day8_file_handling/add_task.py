# add_task.py
# - Ask user for task name
# - Append it to todo.txt

# Define add_task() function
def add_task(task_name: str):
    try:
        filename = "todo.txt"
        with open(filename, "a") as file:
            file.write(f"{task_name}\n")
            print("Task added successfully. ")
    except FileNotFoundError:
        print(f"{filename} does not exist")

# Define main() function
def main():

    task_name = input("Enter the Task name: ")
    add_task(task_name)


if __name__ == "__main__":
    main()