import random

class MYArray():
    def __init__(self, capacity=0, fill_value=0) -> None:
        self.items = [fill_value for _ in range(capacity)]
        self.populate()

    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index=0):
        return self.items[index]

    def __setitem__(self, index=0, value=None):
        self.items[index] = value

    def populate(self):
        for index in range(len(self.items)):
            self.items[index] = random.randint(1,10)

    def __sum__(self):
        total = 0
        for item in self.__iter__():
            total += item
        return total

class Grid:
    """Definition of class Grid, a 2-dimensional table of n rows and m colums"""
    def __init__(self, rows=0, columns=0) -> None:
        self.data = MYArray(rows)
        for index in range(rows):
            self.data[index] = MYArray(columns)
        
        self.populate()

    def __str__(self) -> str:
        output = "\n"
        for row in range(self.get_height()):
            for column in range(self.get_widht()):
                output += str(self.data[row][column]) + " "
            output += "\n"
        return output
    
    def populate(self):
        for row in range(self.get_height()):
            for column in range(self.get_widht()):
                self.data[row][column] = random.randint(1,10)

    def get_height(self):
        return len(self.data)
    
    def get_widht(self):
        return len(self.data[0]) 

    def __getitem__(self, index=0):
        return self.data[index]
    
    def __setitem__(self, row, column, value):
        self.data[row][column] = value

class Cube:
    """Definition of class cube, a 3-dimensional cube of x height, y width and z depth"""
    def __init__(self, rows=0, columns=0, depth=0) -> None:
        self.data = Grid(rows, columns)
        for row in range(rows):
            for column in range(columns):
                self.data[row][column] = MYArray(depth)
        
    def __str__(self) -> str:
        output = "\n"
        for row in range(self.get_height()):
            for column in range(self.get_widht()):
                output += str(self.data[row][column]) + " "
            output += "\n"
        return output
    
    def populate(self):
        for row in range(self.get_height()):
            for column in range(self.get_widht()):
                self.data[row][column] = random.randint(1,10)

    def get_height(self):
        return self.data.get_height()
    
    def get_widht(self):
       return self.data.get_widht()

    def get_depth(self):
        return len(self.data[0][0]) 
    

if __name__ == "__main__":
    menu = MYArray(5)
    print(f"Len method of array: {menu.__len__()}")
    print(f"Str method of array: {menu}")
    print(f"Iter method of array: {menu.__iter__()}")
    print(f"Sum method of array: {menu.__sum__()}")

    grid = Grid(3,4)
    print(f"Str method of grid: {grid}")
    print(f"Get item method of grid: {grid.__getitem__(1)}")

    cube = Cube(3,4,2)
    print(f"Str method of cube: {cube}")
    print(f"Get depth method of cube: {cube.get_depth()}")

    