# delete_task.py
# - Let user choose a task number to remove from the file

# Define delete_task() function
def delete_task(task_num: int):
    try:
        filename = "todo.txt"
        content = []
        with open(filename, "r") as file:
            content = file.readlines()
            content.pop(task_num) if content else print("Todo.txt is empty")
        with open(filename, "w") as file:
            for line in content:
                file.write(line)
        print("Task deleted successfully")
    except FileNotFoundError:
        print(f"{filename} does not exist in this directory")

# Define the main() function
def main():
    task_number = int(input("Enter the task number to be deleted: "))
    delete_task(task_number)

if __name__ == "__main__":
    main()