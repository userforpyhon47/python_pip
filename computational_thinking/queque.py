from stack import Stack
from nodes import TwoWayNode


class ListBasedQueue:
    def __init__(self) -> None:
        self.items = []
    
    def enqueue(self, data):
        self.items.insert(0, data)

    def dequeue(self):
        return self.items.pop()
    
    def __iter__(self):
        return iter(self.items)
    
    def __len__(self):
        return len(self.items)


class StackBasedQueue:
    def __init__(self) -> None:
        self.inbound = Stack()
        self.outbound = Stack()
        self.length = 0
    
    def enqueue(self, data):
        self.inbound.push(data)
        self.length += 1

    def dequeue(self):
        while not self.inbound.is_empty():
            self.outbound.push(self.inbound.pop())
        self.length -= 1
        return self.outbound.pop()

    
    def __len__(self):
        return self.length


class NodeBasedQueue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    
    def enqueue(self, data):
        new_node = TwoWayNode(data)
        current = self.head
       
        if current is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
        
    def dequeue(self):
        current = self.head
        if current:
            self.head = self.head.next
            self.length -= 1
            return current.data        

    def clear(self):
        while self.head:
            self.dequeue()

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __len__(self):
        return self.length    

if __name__ == "__main__":

    fruit_list = ["Banana", "Apple", "Orange", "Strawberry", "Orange", 
                  "Bluberry", "Blackberry", "Cherry", "Pasion Fruit", "Orange", "Apple"]
    
    fruits = NodeBasedQueue()

    print("Initial length:", len(fruits)) # Check length after creating instance
    
    [fruits.enqueue(fruit) for fruit in fruit_list] # Populate data

    print("Initial length:", len(fruits)) # Check length after appending instance

    for fruit in fruits:
        print(fruit)

    print(fruits.dequeue()) # Print Banana
    print(fruits.dequeue()) # Prints Apple
    print(fruits.dequeue()) # Prints Orange

    fruits.clear()
    print(fruits.length) # Prints Orange


