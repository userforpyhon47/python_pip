class Node:
    node_count = 0
    def __init__(self, data=None, next=None) -> None:
        self.name = Node.node_count
        self.data = data
        self.next = next
        Node.node_count += 1
    
    def __str__(self):
        return f"{self.data}"


class TwoWayNode(Node):
    def __init__(self, data=None, previous=None, next=None) -> None:
        super().__init__(data, next)
        self.previous = previous
    
    def __str__(self):
        return f"{self.name}"


if __name__ == "__main__":
   
    head = Node("Head", None)
    for index in range(5):
        head = Node(f"Value: {index}", head)
    
    while head.next is not None:
            print(head)         
            head = head.next


