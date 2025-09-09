#creating own class OOP practice

# Base Class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        # attributes
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in mAh
        self.is_on = False

    # methods
    def power_on(self):
        self.is_on = True
        return f"{self.brand} {self.model} is now ON."

    def power_off(self):
        self.is_on = False
        return f"{self.brand} {self.model} is now OFF."

    def check_storage(self):
        return f"Storage available: {self.storage} GB."

    def __str__(self):
        return f"{self.brand} {self.model} | {self.storage}GB | {self.battery}mAh"


# Inherited Class (Polymorphism Example)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        # call parent constructor
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    # override method (polymorphism)
    def check_storage(self):
        return f"Gaming storage: {self.storage} GB with ultra-fast read/write speeds."

    def enable_gaming_mode(self):
        if self.is_on:
            return f"Gaming mode enabled with {self.cooling_system} cooling!"
        else:
            return "Please power on the device first."


# Demo Usage
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "Galaxy S23", 128, 4000)
    print(phone1)
    print(phone1.power_on())
    print(phone1.check_storage())

    print("----")

    gaming_phone = GamingPhone("Asus", "ROG Phone 7", 512, 6000, "liquid cooling")
    print(gaming_phone)
    print(gaming_phone.power_on())
    print(gaming_phone.check_storage())  # polymorphism: different behavior
    print(gaming_phone.enable_gaming_mode())
