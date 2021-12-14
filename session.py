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


