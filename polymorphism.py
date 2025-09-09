# Activity 2: Polymorphism Challenge 🎭

# Base Class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# Derived Classes
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"


class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"


class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚲"


class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"


# Demo
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Bicycle(), Boat()]

    for v in vehicles:
        print(f"{v.__class__.__name__}: {v.move()}")
