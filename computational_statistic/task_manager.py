def createTaskPlanner():
    task_list = [] # Creamos una variable de lista para guardar las tareas en la función de Closure

    def addTask(task):
        # Desempacamos cada uno de los pares llave: valor con **task y añadimos un par clave: valor extra a un nuevo diccionario
        task = {**task, "completed": False} 
        #Añadimos la tarea a la lista de tareas
        task_list.append(task)

    def searchTask(value):
        #List comprehension para buscar una tarea en particular
        return [task for task in task_list if task.get("id") == value or task.get("name") == value]
    
    def removeTask(value):
        """Buscamos la tarea, como es una lista debemos siempre acceder al primer elemento de la misma
        partiendo de la suposición que las tareas son únicas"""
        task = searchTask(value)
        if task:
            #Si el resultado de la búsqueda contiene un elemento, borramos ese elemento de la lista de tareas
            task_list.remove(task[0])
            return True
        return False
    
    def getTasks():
        return task_list
    
    def getPendingTasks():
        return [ task for task in task_list if task.get("completed") == False]
        
    def getCompletedTasks():
        return [ task for task in task_list if task.get("completed") == True]

    
    def markTaskAsCompleted(value):
        """Buscamos la tarea, como es una lista debemos siempre acceder al primer elemento de la misma
        partiendo de la suposición que las tareas son únicas"""
         
        task = searchTask(value)
        if task:
            #Si el resultado de la búsqueda contiene un elemento, actualizamos su valor de la llave update
            task[0]["completed"] = True
            return True
        return False
    
    def getSortedTasksByPriority():
        """Utilizamos la función sorted donde su parámetro key es una función lambda que recibe cada argumento x
        de la lista task_list y de ese argumento accede a la llave priority para realizar el ordenamiento"""

        return sorted(task_list, key = lambda x: x['priority'])
    
    def filterTasksByTag(tag):
        return [task for task in task_list if tag in task.get("tags")]
    
    def updateTask(taskId, updates):
        """Buscamos la tarea, como es una lista debemos siempre acceder al primer elemento de la misma
        partiendo de la suposición que las tareas son únicas"""
        task = searchTask(taskId)
        if task:
            #Si el resultado de la búsqueda contiene un elemento, encontramos cuál es su indice en la lista de tareas
            index = task_list.index(task[0])
            #Borramos la tarea de la lista de tareas
            task_list.pop(index)
            #Insertamos nuevamente la tarea con las actualizaciones correspondientes en su posición original
            task_list.insert(index, {**task[0], **updates})
            return True
        return False
    
    """Retornamos en un diccionario la llave: valor de las funciones que luego podemos acceder de este closure 
    mediante createTaskPlanner()["llave_funcion"](*args) """

    return {"addTask": addTask,
            "removeTask": removeTask,
            "getTasks": getTasks,
            "getPendingTasks": getPendingTasks,
            "getCompletedTasks": getCompletedTasks,
            "markTaskAsCompleted": markTaskAsCompleted,
            "getSortedTasksByPriority": getSortedTasksByPriority,
            "filterTasksByTag": filterTasksByTag,
            "updateTask": updateTask
            }

if __name__ == "__main__":

    # planner = createTaskPlanner()

    # planner['addTask']({
    #     'id': 1,
    #     'name': 'Comprar leche',
    #     'priority': 1,
    #     'tags': ['shopping', 'home']
    # })

    # planner['addTask']({
    #     'id': 2,
    #     'name': 'Llamar a Juan',
    #     'priority': 3,
    #     'tags': ['personal']
    # })

    # planner['markTaskAsCompleted']('Llamar a Juan')

    # print(planner['getCompletedTasks']())

 
    # [{
    # 'id': 2,
    # 'name': 'Llamar a Juan',
    # 'completed': True,
    # 'priority': 3,
    # 'tags': ['personal']
    # }]

    # planner = createTaskPlanner()

    # planner['addTask']({
    #     'id': 1,
    #     'name': 'Comprar leche',
    #     'priority': 1,
    #     'tags': ['shopping', 'home']
    # })

    # planner['addTask']({
    #     'id': 2,
    #     'name': 'Llamar a Juan',
    #     'priority': 3,
    #     'tags': ['personal']
    # })

    # print(planner['filterTasksByTag']('shopping'))

    # print(planner['filterTasksByTag']('shopping'))



    mytask = createTaskPlanner()
    data_1 = {
            'id': 1,
            'name': 'Comprar leche',
            'priority': 3,
            'tags': ['shopping', 'home']
            }
    
    data_2 = {
            'id': 2,
            'name': 'Comprar pan',
            'priority': 1,
            'tags': ['shopping', 'home']
            }
    
    data_3 = {
            'id': 3,
            'name': 'Comprar huevos',
            'priority': 0,
            'tags': ['shopping', 'home']
            }
    
    mytask["addTask"](data_1)
    mytask["addTask"](data_2)
    mytask["addTask"](data_3)

    print("GET TWO TASKS")
    print(mytask["getTasks"]())

    print("REMOVE TASK 1")
    print(mytask["removeTask"](1))

    print("PRINT REMAINING TASKS")
    print(mytask["getTasks"]())

    print("PRINT PENDING TASKS")
    mytask["addTask"](data_1)
    print(mytask["getPendingTasks"]())

    print("PRINT COMPLETED TASKS")
    print(mytask["getCompletedTasks"]())

    
    print(mytask["markTaskAsCompleted"](2))

    print("PRINT COMPLETED TASKS")
    print(mytask["getCompletedTasks"]())

    print("PRINT PENDING TASKS")
    print(mytask["getPendingTasks"]())

    print("FILTER BY TAG TASKS")
    print(mytask["filterTasksByTag"]("shopping"))
    
    print(mytask["getSortedTasksByPriority"]())
    
    print(mytask["updateTask"](3, {"update_1": 1, "update_2":2, "priority": 5}))

    print("PRINT PENDING TASKS")
    print(mytask["getPendingTasks"]())

