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

#%%

class Invoice:

    def __init__(self, tax, value_before_tax, address, date, due_date):
        self.tax = tax
        self.value_before_tax = value_before_tax
        self.address = address
        self.date = date
        self.due_date = due_date

    def get_final_cost(self):
        return self.value_before_tax + (self.value_before_tax * self.tax)

google_analytics_invoice = Invoice(0.21, 100, "Maria de molina", "2021-21-12", "2021-21-12")

print(google_analytics_invoice.due_date)
print(google_analytics_invoice.get_final_cost())



# %%

class Member:

    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def play(self):
        print(self.name + " plays the " + self.instrument)


class RockBand:

    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def rehearse(self):
        for member in self.members:
            member.play()


john = Member("John", "vocals")
george = Member("George", "guitar")
paul = Member("Paul", "bass guitar")
ringo = Member("Ringo", "drums")
beatles = RockBand()
beatles.add_member(john)
beatles.add_member(george)
beatles.add_member(paul)
beatles.add_member(ringo)

beatles.rehearse()
#%%

class Parent:
    
    def say_hello(self):
        print("hello!")


class Child(Parent):
    pass

child = Child()

child.say_hello()

#%%

class Vehicle:

    def start_engine(self):
        print("BROOM!")


class Car(Vehicle):
    pass

class Tesla(Car):
    
    def start_engine(self):
        print("blip!")

my_car = Car()
my_car.start_engine()

my_tesla = Tesla()
my_tesla.start_engine()





# %%

import math

class GeometryError(ValueError):
    pass

# DRY!

class Shape:

    def __init__(self, name, area):
        self.name = name
        self.area = area
    

class Circle(Shape):
    
    def __init__(self, radius):
        super().__init__("circle", math.pi * radius ** 2)

        self.radius = radius


class Square(Shape):
    
    def __init__(self, side):
        super().__init__("square", side * side)

        self.side = side


circle = Circle(6)
square = Square(3)

print(circle.area)
print(square.area)


#%%

circle = Circle(6)
square = Square(3)

print(type(circle) == Shape)
print(type(square) == Shape)

print(isinstance(circle, Circle))
print(isinstance(circle, Shape))
print(isinstance(square, Shape))

# %%


class Invoice:

    def __init__(self, tax, value_before_tax, address, date, due_date):
        self.tax = tax
        self.__value_before_tax = value_before_tax
        self.address = address
        self.date = date
        self.due_date = due_date

    def get_value_before_tax(self):
        return self.__value_before_tax

    def get_final_cost(self):
        return self.__value_before_tax + (self.__value_before_tax * self.tax)

google_analytics_invoice = Invoice(0.21, 100, "Maria de molina", "2021-21-12", "2021-21-12")

print(google_analytics_invoice.get_value_before_tax())

# print(google_analytics_invoice.get_final_cost())

# %%


# matrix = [
#     [0, 1, 1],
#     [0, 1, 1],
#     [0, 1, 1]
# ]


adjacency_list = {
    "a": ["b"],
    "b": ["a", "c"],
    "c": []
}

#%%

# using adjacency lists

class Vertex:
    def __init__(self, value, additional_info, list_of_edges = []):
        self.value = value
        self.additional_info = additional_info
        self.list_of_edges = list_of_edges

class Edge:
    def __init__(self, origin, destination, weight = None):
        self.origin = origin
        self.destination = destination
        self.weight = weight

class Graph:
    # vertices
    # directionality
    def __init__(self, vertices):
        self.vertices = vertices

    def find_path(self, start, end):
        pass

class DirectedGraph(Graph):
    pass

class UndirectedGraph(Graph):
    pass