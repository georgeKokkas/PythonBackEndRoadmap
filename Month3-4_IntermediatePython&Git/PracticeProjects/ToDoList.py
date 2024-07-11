# This will be a simple command-line to-do list application.

# A simple to-do list application should:

#     Allow the user to add tasks.
#     Allow the user to view tasks.
#     Allow the user to remove tasks.
#     Save tasks to a file.
#     Load tasks from a file.

# Define a function to display the menu and get the user's choice
def display_menu():
    print("To-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Save Tasks")
    print("5. Load Tasks")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    return choice

# Define a function to add a task to the to-do list
def add_task(todo_list):
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f"Task '{task}' added.")

# Define a function to view all tasks in the to-do list
def view_tasks(todo_list):
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Define a function to remove a task from the to-do list
def remove_task(todo_list):
    view_tasks(todo_list)
    if todo_list:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")

# Define a function to save tasks to a file
def save_tasks(todo_list, filename="todo_list.txt"):
    with open(filename, 'w') as file:
        for task in todo_list:
            file.write(task + "\n")
    print(f"Tasks saved to {filename}.")

# Define a function to load tasks from a file
def load_tasks(filename="todo_list.txt"):
    todo_list = []
    try:
        with open(filename, 'r') as file:
            todo_list = [line.strip() for line in file.readlines()]
        print(f"Tasks loaded from {filename}.")
    except FileNotFoundError:
        print(f"No saved tasks found in {filename}.")
    return todo_list

# Main function to run the to-do list application
def main():
    todo_list = []
    while True:
        choice = display_menu()
        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            view_tasks(todo_list)
        elif choice == '3':
            remove_task(todo_list)
        elif choice == '4':
            save_tasks(todo_list)
        elif choice == '5':
            todo_list = load_tasks()
        elif choice == '6':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Call the main function to start the program
if __name__ == "__main__":
    main()
