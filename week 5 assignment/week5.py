# Base class representing a general smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life

    def display_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Battery Life: {self.battery_life} hours"

    def call(self):
        return f"Making a call on the {self.model}."

# Inherited class for a specific smartphone, such as iPhone
class iPhone(Smartphone):
    def __init__(self, model, battery_life, ios_version):
        super().__init__("Apple", model, battery_life)
        self.ios_version = ios_version

    def display_details(self):
        return f"iPhone Model: {self.model}, iOS Version: {self.ios_version}, Battery Life: {self.battery_life} hours"

    # Method override for custom behavior
    def call(self):
        return f"Making a FaceTime call on the {self.model}."

# Inherited class for a specific smartphone, such as Samsung
class Samsung(Smartphone):
    def __init__(self, model, battery_life, android_version):
        super().__init__("Samsung", model, battery_life)
        self.android_version = android_version

    def display_details(self):
        return f"Samsung Model: {self.model}, Android Version: {self.android_version}, Battery Life: {self.battery_life} hours"

    # Method override for custom behavior
    def call(self):
        return f"Making a video call on the {self.model}."

# Test the classes
iphone = iPhone("iPhone 13", 20, "iOS 16")
samsung = Samsung("Galaxy S21", 18, "Android 12")

print(iphone.display_details())  # iPhone details
print(iphone.call())  # iPhone call method

print(samsung.display_details())  # Samsung details
print(samsung.call())  # Samsung call method

#Polymorphism Challenge!
# Base class for vehicles
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Car class implementing move() method
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Plane class implementing move() method
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Test the polymorphism
vehicles = [Car(), Plane()]

for vehicle in vehicles:
    print(vehicle.move())  # Prints either "Driving 🚗" or "Flying ✈️" depending on the object
