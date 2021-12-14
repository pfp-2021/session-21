#%%

class Car:
    pass

car1 = Car()

print(type(car1))

# %%


class Car:

    def __init__(self):
        print("a new car has been instantiated")

car1 = Car()
car2 = Car()
        
# %%

class Car:

    def __init__(self, brand, model):
        accepted_brands = ["Tesla", "Audi"]

        if brand not in accepted_brands:
            raise ValueError("only Teslas and Audis accepted")

        self.brand = brand
        self.model = model


model_s = Car("Tesla", "Model S")
fiesta  = Car("Ford", "Fiesta")

print(model_s.brand + " " + model_s.model)
#print(fiesta.brand + " " + fiesta.model)
# %%

class Clock:

    def __init__(self, hours, minutes):
        if hours < 0 or hours > 23:
            raise ValueError("hours must be 0-23")

        if minutes < 0 or minutes > 59:
            raise ValueError("minutes must be 0-59")

        self.hours = hours
        self.minutes = minutes

    def print_current_time(self):
        print(str(self.hours) + ":" + str(self.minutes))

    def tick(self):
        if self.minutes == 59:
            self.minutes = 0
            if self.hours == 23:
                self.hours = 0
            else:
                self.hours += 1
        else:
            self.minutes += 1

clock1 = Clock(21, 30)

clock1.print_current_time()

import time

for x in range(0, 160):
    time.sleep(1)

    clock1.tick()
    clock1.print_current_time()


# %%

import math

class Shape:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("somethign")

    def calculate_area(self):
        pass

# DRY

class Circle(Shape):

    def __init__(self, radius):
        super().__init__("circle")
        super().say_hello()

        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

class Square(Shape):

    def __init__(self, side):
        super().__init__("square")

        self.side = side

    def calculate_area(self):
        return self.side * self.side

square = Square(2)
circle = Circle(3.2)

# print(square.calculate_area())
# print(circle.calculate_area())


print(type(square) == Shape)
print(isinstance(square, Shape))
# %%


class Invoice:

    def __init__(self, tax, total_value):
        self.tax = tax
        self.__total_value = total_value

    def get_total_value(self):
        return self.__total_value

    def calculate_final_price(self):
        return self.__total_value + (self.tax * self.__total_value)

google_analytics_invoice = Invoice(0.21, 500)

# print(google_analytics_invoice.get_total_value())
# print(google_analytics_invoice.__total_value)

# print(google_analytics_invoice.calculate_final_price())

# %%

# matrices = [
#     [0, 1, 0],
#     [0, 1, 0],
#     [0, 1, 0]
# ]

graph = {
    "a": ["b", "c"],
    "b": [],
    "c": []
}

#%%

class Vertex:
    # value
    # list of edges

    def __init__(self, value, edges = []):
        self.value = value
        self.edges = edges


class Edge:
    # weight
    # from_vertex
    # to_vertex

    def __init__(self, from_vertex, to_vertex, weight = None):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight


class Graph:
    # vertices
    # directed/undirected

    def __init__(self):
        self.vertices = []
        # self.directed = directed

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

class DiGraph(Graph):
    # Directed graphs

    pass

class UndirectedGraph(Graph):
    #
    pass
