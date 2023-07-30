from nodes import Node


class SingleLinkedList:
    def __init__(self) -> None:
        self.head = Node("HEAD")
        self.length = 0

    def __iter__(self):
        current_node = self.head

        while current_node.next:
            current_node = current_node.next
            yield current_node.data
    
    def append(self, data):
        current_node = self.head
        
        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data)
        self.length += 1
    
    def delete(self, data):
        current_node = self.head

        while current_node.next:
            prev_node = current_node
            current_node = current_node.next
            if current_node.data == data:
                prev_node.next = current_node.next
                del current_node
                current_node = prev_node
                self.length -= 1
    
    def replace(self, data, new_data):
        current_node = self.head
    
        while current_node.next:
            current_node = current_node.next
            if current_node.data == data:
                current_node.data = new_data
    
    def remove(self, index=0):
        current_node = self.head
        counter = 0
        while current_node.next:
            prev_node = current_node
            current_node = current_node.next
            if counter == index:
                prev_node.next = current_node.next
                print(f" Deleted {current_node.data}")
                del current_node
                self.length -= 1
                break
            counter += 1
    
    def insert(self, index=0, data=""):
        current_node = self.head
        counter = 0
        while current_node.next:
            prev_node = current_node
            current_node = current_node.next
            if counter == index:
                current_node = Node(data, current_node)
                prev_node.next = current_node
                self.length += 1
                break
            counter += 1

    def clear(self):
        for item in self:
            self.delete(item)

    def search(self, data):
        for node in self:
            if node == data:
                print(f"found {node}")

    def length(self):
        return str(self.length)



if __name__ == "__main__":
    fruit_list = ["Banana", "Apple", "Orange", "Strawberry", "Orange", 
                  "Bluberry", "Blackberry", "Cherry", "Pasion Fruit", "Orange", "Apple"]
    fruits = SingleLinkedList()
    print("Initial length:",fruits.length) # Check length after creating instance
    
    [fruits.append(fruit) for fruit in fruit_list] # Populate data
    
    print("Lenght after population: ", fruits.length) # Check length after adding items

    print("Printing populated data") # Check length after adding items
    for fruit in fruits: # Use __iter__ method to print object's items after adding
        print(" ", fruit)
    
    fruits.search("Orange") # Use Search method to search item

    fruits.delete("Orange") # Use Delete method to delete item
    
    print("Lenght after deletion of item Orange:", fruits.length) # Check length after deleting items

    print("Printing after deletion") # Check length after deleting items
    for fruit in fruits: # Use __iter__ method to print object's items after deletion
        print(" ", fruit)

    print("Printing after replacing") # Check length after deleting items
    fruits.replace("Apple", "Watermelon")

    for fruit in fruits: # Use __iter__ method to print object's items after clearing
        print(" ", fruit)


    print("Printing after removing index") # Check length after deleting items
    fruits.remove(1)


    for fruit in fruits: # Use __iter__ method to print object's items after clearing
        print(" ", fruit)


    print("Printing after inserting index") # Check length after deleting items
    fruits.insert(6, "test")

    for fruit in fruits: # Use __iter__ method to print object's items after clearing
        print(" ", fruit)
    
    fruits.clear() # User Clear method to delete all objtect´s items

    for fruit in fruits: # Use __iter__ method to print object's items after clearing
        print(" ", fruit)

    print("Length after clearing", fruits.length) # Check length after clearing items
