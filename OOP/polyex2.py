class Car:

    def __init__(self, make, model):
        self.make = make
        self.model = model


    def move(self):
        print("Driving around")

class Plane:

    def __init__(self,make,model):
        self.make = make
        self.model = model

    def move(self):
        print("Fly around")


class Motorbike:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def move(self):
        print("Ride around")

#instance our class

car = Car("Note", "Satrit")
plane = Plane("Boeing", "737")
bike = Motorbike("Kawaski", "Ninja650")

for i in (car, plane, bike):
    i.move()