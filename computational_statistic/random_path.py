import random

from bokeh.plotting import figure, show


class Drunk:
    def __init__(self, name: str="") -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name
    

class Coordinate:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def get_distance(self, coordinate):
        return ((coordinate.x - self.x) ** 2 + (coordinate.y - self.y) ** 2) ** 0.5
    
    def move_coordinate(self, new_x, new_y):
        self.x = self.x + new_x
        self.y = self.y + new_y
        return Coordinate(self.x, self.y)
    
    def __str__(self):
        return f"{self.x}, {self.y}"
        

class TraditionalDrunk(Drunk):
    def __init__(self, name) -> None:
        super().__init__(name)
      
    def move_drunk(self):
        return random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
        

class Field:
    def __init__(self) -> None:
        self.drunks_coordinates = {}
    
    def add_drunk(self, drunk, coordinate):
        self.drunks_coordinates[drunk] = coordinate
        
    def move_drunk(self, drunk: TraditionalDrunk):
        new_x, new_y = drunk.move_drunk()
        current_coordinate = self.drunks_coordinates[drunk]
        new_coordinate = current_coordinate.move_coordinate(new_x, new_y)
        self.drunks_coordinates[drunk] = new_coordinate
        return new_coordinate
    
    def get_drunk_coordinate(self, drunk: TraditionalDrunk):
        return self.drunks_coordinates[drunk]
    

def aux(field: Field, step, drunk):
    coordinates_x = []
    coordinates_y = []

    for _ in range(step):
        coordinate = field.move_drunk(drunk)
        coordinates_x.append(coordinate.x)
        coordinates_y.append(coordinate.y)


    # create a new plot with a title and axis labels
    p = figure(title="Random Walk", x_axis_label='x', y_axis_label='y')
    # add a line renderer with legend and line thickness to the plot
    p.line(coordinates_x, coordinates_y, legend_label="Temp.", line_width=2)
    # show the results
    show(p)

    return field.get_drunk_coordinate(drunk)

def move(step, times, drunk):
    origin = Coordinate()
    field = Field()
    field.add_drunk(drunk, origin)
    distance = []
    for _ in range(times):
        coordinate = aux(field, step, drunk)
        distance.append(origin.get_distance(coordinate))
    return distance

def main(steps, times, drunk):
    for step in steps:
        distance = move(step, times, drunk)
        print(f"{step} walk distances {times} times: {distance}")

if __name__ == "__main__":
    steps = [int(1e4)]
    times = 1
    drunk = TraditionalDrunk("Nobody")
    main(steps, times, drunk)

