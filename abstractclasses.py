from abc import ABC, abstractmethod


# Abstract class creates an template which all the child classes must follow.
# Example of an Abstract class
class Vehicle(ABC):
    
    @abstractmethod
    def headlight(self):
        pass

    @abstractmethod
    def brakes(self):
        pass


class Benz(Vehicle):

    def headlight(self):
        print("Working headlight")

    def brakes(self):
        print("Working Brakes")

class Activa(Vehicle):

    def brakes(self):
        print("Working Brakes")

# Vehicle1 doesn't throw an exception because it has followed all the method rules by abstract class Vehicle
vehicle1 = Benz()

# Vehicle2 throws an error because it didn't follow all the method rules by abstract class Vehicle
# Error Received: "TypeError: Can't instantiate abstract class Activa with abstract methods headlight"
vehicle2 = Activa()