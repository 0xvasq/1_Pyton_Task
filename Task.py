class Task():
    def __init__(self, taskID, taskTitle, taskDesc, taskPriority, taskStatus):
        self.taskID = taskID
        self.title = taskTitle
        self.descrp = taskDesc
        self.prtyLevel = taskPriority
        self.status = taskStatus

    def setID(self, newID):
        try:
            self.taskID = int(newID)
        except ValueError:
            print("Error: ID must be an integer")


    def getID(self):
        return self.taskID

    def setTitle(self, newTitle):
        if newTitle:
            self.title = newTitle
        else:
            self.title = "Untitled"

    def getTitle(self):
        return self.title

    def setdescrp(self, newDescrp):
        if newDescrp:
            self.descrp = newDescrp
        else:
            self.descrp = "N/a"

    def getDescrp(self):
        return self.descrp

    def setPrtyLevel(self, newPrtyLevel):
        try:
            self.prtyLevel = int(newPrtyLevel)
        except ValueError:
            print("Error: the task must have a priority level from Easy to Urgent")

    def getPrtyLevel(self):
        return self.prtyLevel

    def setStatus(self, newStatus):
       
        if newStatus:
            self.status = "Completed"

        else: 
            self.status = "Pending"

    def getStatus(self):
        return self.status

  