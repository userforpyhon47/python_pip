class ContactList:
    def __init__(self, size):
        self.data = [ [] for _ in range(size)]
        self.length = size
    
    def hash(self, key):
        return hash(key) % self.length

    def insert(self, name, phone):
        self.data[self.hash(name)].append([name, phone])

    def get(self, name):
        for item in self.data[self.hash(name)]:
            if item[0] == name:
                return item[1]
        
    def retrieveAll(self):
        output = []
        for item in self.data:
            output.extend(item)
        return output[:]

    def delete(self, name):
        for index, item in enumerate(self.data[self.hash(name)]):
            if item[0] == name:
                self.data[self.hash(name)][index] = []
            break


if __name__ == "__main__":
    phone_book = ContactList(10)
    
    #test_data = [phone_book.insert(item, item*2) for item in range(10)]

    phone_book.insert("Mr Michi", "123-456-7890")
    phone_book.insert("Mr firulais", "123-456-7890")

    phone_book.insert("10", "123-456-7890")

    phone_book.insert("10", "123-456-7890")



    print("Getting items")
    for item in range(10):
        print(phone_book.get(item))

    print(phone_book.get(60))

    print("Retrieving items")
    print(phone_book.retrieveAll())

    # print("Deleting items")
    # for item in range(10):
    #     print(phone_book.delete(item))