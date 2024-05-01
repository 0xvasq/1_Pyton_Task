from Task import Task


class TaskManager():
    def __init__(self):
        self.tasks = []

    def addTask(self, taskID, taskTitle, taskDesc, taskPrty, taskStatus):
        newTask = Task(taskID, taskTitle, taskDesc,taskPrty, taskStatus)
        self.tasks.append(newtask)

    def markTaskCompleted(self, taskID):
        for task in self.tasks:
             if task.taskID == taskID:
                task.taskStatus = "Completed"




