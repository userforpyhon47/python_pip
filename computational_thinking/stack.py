from nodes import Node

class Stack:
    def __init__(self) -> None:
        self.top = None
        self.lenght = 0

    def push(self, data):
        new_node = Node(data)
        
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.lenght += 1

    def __iter__ (self):
        current_node = self.top

        while current_node:
            yield current_node.data
            current_node = current_node.next
            
    def __len__(self):
        return self.lenght
    
    def get_top(self):
        return self.top
    
    def pop(self):
        current_top = self.top
        if current_top:
            del self.top
            self.lenght -= 1
            self.top = current_top.next
        
        return current_top
    
    def clear(self):
        while self.top:
            self.pop()
    
    def is_empty(self):
        return self.lenght == 0
    
   
if __name__ == "__main__":
   
    fruit_list = ["Banana", "Apple", "Orange", "Strawberry", "Orange", 
                  "Bluberry", "Blackberry", "Cherry", "Pasion Fruit", "Orange", "Apple"]
    
    fruits = Stack()

    print("Initial length:", len(fruits)) # Check length after creating instance
    
    [fruits.push(fruit) for fruit in fruit_list] # Populate data

    print("Actual length:", len(fruits)) # Check length after appending instance

    for fruit in fruits:
        print(fruit)

    print(fruits.pop())
    print(fruits.pop())
    print(fruits.pop())

    print(fruits.get_top())

    fruits.clear()

    print(fruits.get_top())

    print(fruits.is_empty())



