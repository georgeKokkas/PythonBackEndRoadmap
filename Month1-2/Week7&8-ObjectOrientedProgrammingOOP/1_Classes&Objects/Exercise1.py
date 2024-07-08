# Create a class Person with attributes for name and age. 
# Add a method to display a greeting message. 
# Create objects of the Person class and call the greeting messages.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and i am {self.age} years old."
    
person1 = Person("George", 36)
person2 = Person("Stacy", 28)

print(person1.greet())
print(person2.greet())