class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.data = self.get_data()
        self.length = 0

    def append(self, item):
        new_item = Node(item)
        if self.head == None:
            self.head = new_item
            self.tail = self.head
        else:
            self.tail.next = new_item
            new_item.previous = self.tail
            self.tail = new_item

        self.length += 1

    def pop(self):
        last_node = self.tail
        if self.length > 1:
            self.tail = last_node.previous
            self.tail.next = None
            self.length -= 1
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1

        return last_node.data if last_node else None

    def shift(self):
        first_node = self.head
        if self.length > 1:
            self.head = first_node.next
            self.head.previous = None
            self.length -= 1
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1

        return first_node.data if first_node else None

    def unshift(self, item):
        new_node = Node(item)
        
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node

        self.length += 1
           
    def map(self, func):
        new_list = MyList()
        [new_list.append(func(item)) for item in self]
        return new_list
    
    def filter(self, func):
        new_list = MyList()
        [new_list.append(item) for item in self if func(item)]
        return new_list

    def join(self, character=","):
        output = ""
        for item in self:
            output += str(item) + f"{character}"
        return output.rstrip(character)

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next

    def __len__(self):
        return self.length
    
    def get_data(self):
        return [{index, item} for index, item in enumerate(self)]
  

if __name__ == "__main__":
    number_list = [x for x in range(10)]
    my_list = MyList()
    [my_list.append(item) for item in number_list]

    print("Len after adding", len(my_list))

    print("Printing items")
    for item in my_list:
        print(item)

    print("Filtering items")
    
    result = my_list.filter(lambda x: x>5)
    print(result.__class__)

    print("Printing filtered items")

    for item in result:
        print(item)


    print("Mapping items")

    result = my_list.map(lambda x: x-1)
    print(result.__class__)

    print("Printing mapped items")
    
    for item in result:
        print(item)

    print("Inserting at first position items")
    my_list.unshift(-5)
    my_list.unshift(-4)
    for item in my_list:
        print(item)

    print(len(my_list))


    print("Joining elements")
    print(my_list.join())


    # print("Shifting-deleting first position item")

    # for _ in range(len(my_list)):
    #     print(my_list.shift())
    # print(my_list.shift())
    # print(my_list.shift())

    # for _ in range(len(my_list)):
    #     print(my_list.pop())
    # print(my_list.pop())
    # print(my_list.pop())

  
    #print(len(my_list))


    print(my_list.get_data())