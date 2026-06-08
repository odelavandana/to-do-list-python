
tasks = []  

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

   
    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("task added successfully!")

   
    elif choice == "2":
        if len(tasks) == 0:
            print(" No tasks found!")
        else:
            print("\n Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    
    elif choice == "3":
        print(" Exiting To-Do List. Goodbye!")
        break

   
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")