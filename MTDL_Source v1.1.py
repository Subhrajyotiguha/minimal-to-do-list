todo_list = []

def show_menu():
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task: ")
        todo_list.append(task)
        print("Task added.")
    elif choice == '2':
        if not todo_list:
            print("Your to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for idx, task in enumerate(todo_list, 1):
                print(f"{idx}. {task}")
    elif choice == '3':
        if not todo_list:
            print("Your to-do list is empty.")
            continue
        else:
            print("\nYour Tasks:")
            for idx, task in enumerate(todo_list, 1):
                print(f"{idx}. {task}")
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    elif choice == '4':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
