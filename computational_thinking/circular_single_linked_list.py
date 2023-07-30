from single_linked_list import SingleLinkedList
from nodes import Node


class CircularSingleLinkedList(SingleLinkedList):
    def __init__(self) -> None:
        super().__init__()
        self.head.next = self.head
        self.next_item = self.head.next

    def append(self, data):
        new_node = Node(data)
        current_node = self.head

        while current_node.next != self.head:
            current_node = current_node.next

        current_node.next = new_node
        new_node.next = self.head

        self.length += 1

    def __iter__(self):
        current_node = self.head

        while current_node.next != self.head:
            current_node = current_node.next
            yield current_node.data
    
    def next(self):
        output = self.next_item
        
        if self.next_item == self.head:
            output = self.next_item.next
            if output == self.head:
                return None
            self.next_item = self.next_item.next.next
        else:
            self.next_item = self.next_item.next
            
        return output.data

if __name__ == "__main__":
    fruit_list = ["Banana", "Apple", "Orange", "Strawberry", "Orange", 
                "Bluberry", "Blackberry", "Cherry", "Pasion Fruit", "Orange", "Apple"]
    fruits = CircularSingleLinkedList()
    print("Initial length:",fruits.length) # Check length after creating instance

    [fruits.append(fruit) for fruit in fruit_list] # Populate data

    print("Lenght after population: ", fruits.length) # Check length after adding items

    print("Printing populated data") # Check length after adding items
    for fruit in fruits: # Use __iter__ method to print object's items after adding
        print(" ", fruit)

    for _ in range(16):
        print("-", fruits.next())
