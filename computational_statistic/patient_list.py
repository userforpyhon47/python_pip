class PatientNode:
    def __init__(self, name, age, bed_number):
        self.name = name
        self.age = age
        self.bed_number = bed_number
        self.next = None

    def __str__(self):
        return {"name": self.name, 
                "age": self.age,
                "bedNumber": self.bed_number}

class PatientList:
    def __init__(self, max_bed) -> None:
        
        self.head = PatientNode("HEAD", None, None)
        self.max_bed = max_bed
        self.length = 0

    def __iter__(self):
        current_node = self.head

        while current_node.next:
            current_node = current_node.next
            yield current_node

    def __len__(self):
        return self.length
   
    def addPatient(self, name, age):
        self.length += 1

        current_node = self.head
        
        if self.length > self.max_bed:
            raise Exception("No hay camas disponibles")

        while current_node.next:
            current_node = current_node.next

        current_node.next = PatientNode(name, age, self.length)
    
    def removePatient(self, name):
        current_node = self.head

        while current_node.next:
            prev_node = current_node
            current_node = current_node.next
            if current_node.name == name:
                prev_node.next = current_node.next
                del current_node
                current_node = prev_node
                self.length -= 1
                return current_node.__str__()
        
        raise Exception("Paciente no encontrado")
    
    def getPatient(self, name):
        for node in self:
            if node.name == name:
                return node.__str__()
        raise Exception("Paciente no encontrado")

    def getPatientList(self):
        return [patient.__str__() for patient in self]
   
    def getAvailableBeds(self):
        return self.max_bed - self.length
    
if __name__ == "__main__":
    list = PatientList(3)
    list.addPatient("Paciente 1", 20)
    list.addPatient("Paciente 2", 30)
    list.addPatient("Paciente 3", 40)
    #list.addPatient("Paciente 4", 40)

    print(list.getPatientList())
    print(list.removePatient("Paciente 2"))
    print(list.getPatientList())
    print(list.getAvailableBeds())
