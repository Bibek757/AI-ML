


tasks = []
 
 
def show_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
        return
    for i in range(len(tasks)):
        print(i + 1, "-", tasks[i])
 
 
def add_task(task):
    tasks.append(task)
    print("Added:", task)
 
 
def remove_task(index):
    if index < 1 or index > len(tasks):
        print("Invalid task number.")
        return
    removed = tasks.pop(index - 1)
    print("Removed:", removed)
 
 
def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
    print("Tasks saved to tasks.txt")
 
 
def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass
 
 
def todo_list():
    load_tasks()
    print("To-Do List")
    print("Commands: add, remove, show, save, exit")
 
    while True:
        command = input("\nEnter command: ")
 
        if command == "exit":
            print("Goodbye!")
            break
 
        elif command == "add":
            task = input("Enter task: ")
            add_task(task)
 
        elif command == "remove":
            show_tasks()
            num = int(input("Enter task number to remove: "))
            remove_task(num)
 
        elif command == "show":
            show_tasks()
 
        elif command == "save":
            save_tasks()
 
        else:
            print("Invalid command. Try again.")
 
 
todo_list()
 