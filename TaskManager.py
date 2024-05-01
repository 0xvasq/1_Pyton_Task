from Task import Task


class TaskManager():
    def __init__(self):
        self.tasks = []

    def addTask(self, taskID, taskTitle, taskDesc, taskPrty, taskStatus):
        newTask = Task(taskID, taskTitle, taskDesc,taskPrty, taskStatus)
        self.tasks.append(newTask)

    def markTaskCompleted(self, taskID):
        for task in self.tasks:
             if task.taskID == taskID:
                task.taskStatus = "Completed"

    def viewTask(self):
        print("All tasks: ")
        for task in self.tasks:
            print(task.getID())
            print(task.getTitle())
            print(task.getDescrp())
            print(task.getPrtyLevel())
            print(task.getStatus())

