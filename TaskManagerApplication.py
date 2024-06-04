
tasks = []


def main():
    message = """1- add tasks to a list
    2- mark task as complete
    3- view tasks
    4- Quit"""

    while True:
        print(message)
        choice = input("Enter your choice :")
        if choice == "1":
            add_task()
        elif choice == "2":
            mark_task_complete()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice, Please Enter a number between 1 and 4 :")


def add_task():
    task = input("Enter task :")
    task_info = {'task': task, 'completed': False}
    tasks.append(task_info)
    print("The task added successfuly.")


def mark_task_complete():
    incompleted_tasks = []
    incompleted_tasks = [task for task in tasks if task["completed"] == False]
    if not incompleted_tasks:
        print("No tasks to mark as complete.")
        return
    for i, task in enumerate(incompleted_tasks):
        print(f"{i+1}- {task['task']}")
        print("."*60)
    try:
        task_number = int(input("Choose the task number to complete : "))
        if task_number < 1 or task_number > len(incompleted_tasks):
            print("Invalid task number")
            return
        incompleted_tasks[task_number-1]["completed"] = True
        print("Task marked completed.")
    except ValueError:
        print("Invalid input, please enter a number")


def view_tasks():
    if not tasks:
        print("No tasks to view.")
        return
    for i, task in enumerate(tasks):
        status = "✔" if task['completed'] else "❌"
        print(f"{i+1}. {task['task']} {status}")


main()
