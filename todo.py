# to_do_list.py

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' deleted.")
    else:
        print("Invalid task number.")

while True:
    print("\nOptions: 1. Add Task  2. View Tasks  3. Delete Task  4. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        task_number = int(input("Enter task number to delete: "))
        delete_task(task_number)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
