# Add class methods and static methods to the Person class. 
# Create class methods to instantiate a person from birth year and a static method to check if a person is a minor.

class Person:
    # Define the initializer method to set name and age attributes
    def __init__(self, name, age):
        self.name = name  # Set the name attribute
        self.age = age    # Set the age attribute

    # Define a method to display a greeting message
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    # Define a class method to create a person from birth year
    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2024  # Set the current year
        age = current_year - birth_year  # Calculate the age
        return cls(name, age)  # Return a new instance of the class

    # Define a static method to check if a person is a minor
    @staticmethod
    def is_minor(age):
        return age < 18  # Return True if age is less than 18, else False

# Create instance using the class method    
person1 = Person.from_birth_year('George', 2010)

# Create instance of the class
person2 = Person('Stacy', 28)

# Call the greet method and print the greeting message
print(person1.greet()) # Output: Hello, my name is Charlie and I am 14 years old.
print(person2.greet()) # Output: Hello, my name is Stacy and I am 28 years old.

# Check if the person is a minor using the static method
print(Person.is_minor(person1.age)) # Output: True
print(Person.is_minor(person2.age)) # Output: False