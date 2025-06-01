import json
import os

def show_menu():
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

tasks = []

TASKS_FILE = "tasks.json"

# Load tasks from file if it exists
if os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "r") as file:
        tasks = json.load(file)
else:
    tasks = []

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task_name = input("Enter the task: ")
        task = {"name": task_name, "completed": False}
        tasks.append(task)
        save_tasks()
        print(f"Task '{task_name}' added.")
    elif choice == '2':
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                status = "✅" if task["completed"] else "❌"
                print(f"{index}. {task['name']} [{status}]")
    elif choice == '3':
        if not tasks:
            print("No tasks to mark as completed.")
        else:
            print("\nSelect a task to mark as completed:")
            for index, task in enumerate(tasks, start=1):
                status = "✅" if task["completed"] else "❌"
                print(f"{index}. {task['name']} [{status}]")

            try:
                task_num = int(input("Enter task number: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["completed"] = True
                    save_tasks()
                    print(f"Task '{tasks[task_num - 1]['name']}' marked as completed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == '4':
        if not tasks:
            print("No tasks to delete.")
        else:
            print("\nSelect a task to delete:")
            for index, task in enumerate(tasks, start=1):
                status = "✅" if task["completed"] else "❌"
                print(f"{index}. {task['name']} [{status}]")

            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    save_tasks()
                    print(f"Task '{removed_task['name']}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    elif choice == '5':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")