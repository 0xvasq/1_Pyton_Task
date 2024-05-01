from TaskManager import TaskManager


def menuOptions():
    print("Main Menu:")
    print("1. Add Task")
    print("2. View Tasks")

def addTask(task_manager):
    task_id = input ("Enter task ID: ")
    task_title = input ("Enter task title: ")
    task_desc = input ("Enter task description: ")
    task_prty = input ("Enter task priority: ")
    task_status = input("Enter the task status: ")
    task_manager.addTask(task_id, task_title,task_desc, task_prty, task_status)

def viewTasks(task_manager):
    task_manager.viewTask()

def main():
    task_manager = TaskManager()

    while True:
        menuOptions()

        choice = input("Enter your choise. ")

        if choice == "1":
            addTask(task_manager)
        elif choice == "2":
            viewTasks(task_manager)

if __name__ == "__main__":
    main()


