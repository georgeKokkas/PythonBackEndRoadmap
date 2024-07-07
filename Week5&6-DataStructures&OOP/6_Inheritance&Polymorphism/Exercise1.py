# Create a base class Vehicle with attributes for make and model. 
# Add a method to display vehicle details.
# Create derived classes Car and Motorcycle that inherit from Vehicle 
# and override the method to include additional details specific to each type.

# Define a base class named 'Vehicle'
class Vehicle:
    # Define the initializer method to set make and model attributes
    def __init__(self, make, model):
        self.make = make    # Set the make attribute
        self.model = model  # Set the model attribute

    # Define a method to display vehicle details
    def display_info(self):
        return f"Vehicle Make: {self.make}, Model: {self.model}"

# Define a derived class named 'Car' that inherits from 'Vehicle'
class Car(Vehicle):
    # Define the initializer method to set make, model, and doors attributes
    def __init__(self, make, model, doors):
        super().__init__(make, model)  # Call the base class initializer
        self.doors = doors  # Set the doors attribute

    # Override the display_info method to include additional details
    def display_info(self):
        return f"Car Make: {self.make}, Model: {self.model}, Doors: {self.doors}"

# Define a derived class named 'Motorcycle' that inherits from 'Vehicle'
class Motorcycle(Vehicle):
    # Define the initializer method to set make, model, and type attributes
    def __init__(self, make, model, motorcycle_type):
        super().__init__(make, model)  # Call the base class initializer
        self.motorcycle_type = motorcycle_type  # Set the motorcycle_type attribute

    # Override the display_info method to include additional details
    def display_info(self):
        return f"Motorcycle Make: {self.make}, Model: {self.model}, Type: {self.motorcycle_type}"

# Create objects of 'Car' and 'Motorcycle' classes
car = Car("Toyota", "Corolla", 4)
motorcycle = Motorcycle("Harley-Davidson", "Street 750", "Cruiser")

# Call the display_info method and print the details
print(car.display_info())  # Output: Car Make: Toyota, Model: Corolla, Doors: 4
print(motorcycle.display_info())  # Output: Motorcycle Make: Harley-Davidson, Model: Street 750, Type: Cruiser
