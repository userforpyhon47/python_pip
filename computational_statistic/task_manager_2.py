class TaskManager:
  def __init__(self):
    self.task = {}

  def addTask(self, task, tags):
    task = task.lower()
    self.task[task] = self.task.get(task, set()).union(set(tags))

  def printTasks(self):
    return self.task

myTaskManager = TaskManager()
myTaskManager.addTask("Comprar leche", ["compras", "urgente"])
myTaskManager.addTask("Sacar al perro", ["mascotas"])
myTaskManager.addTask("Hacer ejercicio", ["salud"])
myTaskManager.addTask("Comprar leche", ["lacteos"])

print(myTaskManager.printTasks())