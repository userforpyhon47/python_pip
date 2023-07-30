from nodes import TwoWayNode

class DoublyLinkedList():
    def __init__(self) -> None:
        self.head = TwoWayNode("HEAD")
        self.tail = self.head
        
        self.length = 0
    
    def append(self, data): 
        current_node = self.head
        
        while current_node.next:
            current_node = current_node.next

        current_node.next = TwoWayNode(data, self.tail)

        self.tail = current_node.next       

        self.length += 1
    
    def __len__(self):
        return self.length
    
    def forward(self):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            yield current_node
    
    def reverse(self):
        current_node = self.tail
        while current_node.previous and current_node.previous != self.head:
            current_node = current_node.previous
            yield current_node
    
    def get_tail(self):
        return self.tail

    def get_head(self):
        return self.head.next

if __name__ == "__main__":

    fruit_list = ["Banana", "Apple", "Orange", "Strawberry", "Orange", 
                  "Bluberry", "Blackberry", "Cherry", "Pasion Fruit", "Orange", "Apple"]
    
    fruits = DoublyLinkedList()

    print("Initial length:", len(fruits)) # Check length after creating instance
    
    [fruits.append(fruit) for fruit in fruit_list] # Populate data

    print("Initial length:", len(fruits)) # Check length after appending instance


    for fruit in fruits.forward():
        print(" ", fruit.data)

    print(fruits.get_head())
    print(fruits.get_tail())

    for fruit in fruits.reverse():
        print(" ", fruit.data)