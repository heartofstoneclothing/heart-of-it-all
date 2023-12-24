# Simple To-Do List Application in Python

def display_tasks(tasks):
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "[X]" if task['completed'] else "[ ]"
        print(f"{i}. {status} {task['description']}")

def add_task(tasks, description):
    tasks.append({'description': description, 'completed': False})
    print(f"Task '{description}' added to the to-do list.")

def mark_completed(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"Task '{tasks[task_index]['description']}' marked as completed.")
    else:
        print("Invalid task number.")

def remove_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['description']}' removed from the to-do list.")
    else:
        print("Invalid task number.")

def main():
    tasks = []

    while True:
        print("\nOptions:")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("0. Exit")

        choice = input("Enter choice (0-4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == '3':
            display_tasks(tasks)
            task_index = int(input("Enter task number to mark as completed: ")) - 1
            mark_completed(tasks, task_index)
        elif choice == '4':
            display_tasks(tasks)
            task_index = int(input("Enter task number to remove: ")) - 1
            remove_task(tasks, task_index)
        elif choice == '0':
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 4.")

if __name__ == "__main__":
    main()
