# Initialize the to-do list as an empty list
todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Added task: {task}")

def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print(f"Removed task: {task}")
    else:
        print(f"Task '{task}' not found in the to-do list.")

def display_tasks():
    if not todo_list:
        print("The to-do list is empty.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Display tasks")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            task = input("Enter the task to add: ").strip()
            add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ").strip()
            remove_task(task)
        elif choice == '3':
            display_tasks()
        elif choice == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")