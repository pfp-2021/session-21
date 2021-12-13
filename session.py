#%%

class Car:
    pass


volvo = Car()
seat = Car()

print(type(volvo))
print(type(seat))

#%%

class Car:

    def __init__(self, brand, model):
        accepted_brands = ["Tesla", "BMW"]
        
        if brand not in accepted_brands:
            raise ValueError("Brand is not valid")

        self.brand = brand
        self.model = model
        print("a new car has been created!")

model_s = Car("Tesla", "Model S")
fiesta = Car("Ford", "Fiesta")

print(model_s.brand)
print(fiesta.brand)

#%%

class Clock:

    def __init__(self, hours, minutes):
        if type(hours) is not int or type(minutes) is not int:
            raise TypeError("hours and minutes must be integers")

        if hours < 0 or hours > 23:
            raise ValueError("hours must be between 0 and 23")

        if minutes < 0 or minutes > 59:
            raise ValueError("minutes must be between 0 and 59")

        self.hours = hours
        self.minutes = minutes

    def tick(self):
        if self.minutes == 59:
            self.minutes = 0
            if self.hours == 23:
                self.hours = 0
            else:
                self.hours += 1
        else:
            self.minutes += 1

    def print_time(self):
        print(str(self.hours) + ":" + str(self.minutes))

import time

clock = Clock(22, 25)

# while True:
#     time.sleep(1)
#     clock.tick()
#     clock.print_time()



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
paul = Member("Paul", "bass")
george = Member("George", "guitar")
ringo = Member("Ringo", "drums")

beatles = RockBand()
beatles.add_member(john)
beatles.add_member(paul)
beatles.add_member(george)
beatles.add_member(ringo)
beatles.rehearse()




#%%

class Parent:

    def say_hello(self):
        print("hello!")

class Child(Parent):
    pass

object = Child()
object2 = Parent()

object.say_hello()
object2.say_hello()

#%%

class FormField:
    def validate(self):
        pass

class EmailField(FormField):
    pass

class DateField(FormField):
    pass









#%%

class MotorVehicle:
    def start(self):
        print("brooom!!")

class Car(MotorVehicle):
    pass

class Tesla(Car):
    def start(self):
        print("piiip")


fiesta = Car()
fiesta.start()

model_s = Tesla()
model_s.start()



# %%

from math import pi

class Shape:
    def calculate_area(self):
        raise ValueError("calculate_area not implemented")


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2

class Square(Shape):

    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side

circle = Circle(2.3)
square = Square(6)

print(circle.calculate_area())
print(square.calculate_area())

class SetOfShapes:

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        if not isinstance(shape, Shape):
            raise TypeError("shape should be a Shape")

        self.shapes.append(shape)
    

shapes = SetOfShapes()

circle = Circle(3.2)

print(type(circle))

shapes.add_shape(circle)

# %%

class FormValidationError(ValueError):
    pass

class InvalidEmailError(FormValidationError):
    pass

class UnderAgeError(FormValidationError):
    pass

age = 12

if age < 18:
    raise ValueError()

# %%
