# 🏆 Mini Project: To-Do List Manager

# Build a simple command-line to-do list app:
# - Show a menu:
#   1. Add task
#   2. View tasks
#   3. Remove task
#   4. Exit
# - Store tasks in a list
# - Use a loop to keep showing the menu


def show_menu():
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit ")

def add_task(item, list):
    list.append(item)

def view_tasks(list):
    for i in range(len(list)):
        print(f"{i + 1}. {list[i]}")

def remove_task(item, list):
    list.remove(item)
    view_tasks(list)

def exit():
    exit

def main():
    tasks = []

    show_menu()

    while True:
        user_input = input("Enter the corresponding number of you want to do: ")
        if user_input == "1":
            item = input("Enter the task to be added: ")
            add_task(item, tasks)
            view_tasks(tasks)
        elif user_input == "2":
            view_tasks(tasks)
        elif user_input == "3":
            item = input("Enter the task to be removed: ")
            remove_task(item, tasks)
        else:
            break

if __name__ == "__main__":
    main()
