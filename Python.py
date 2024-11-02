class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)  # Calls the parent class constructor
        self.salary = salary

employee = Employee("Alice", 50000)
print(employee.name)   # Output: Alice
print(employee.salary) # Output: 50000

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Output: Woof! Meow


    class Dog:
    def __init__(self, name, breed):  # Constructor method
        self.name = name  # Instance variable
        self.breed = breed
    
    def bark(self):  # Method for behavior
        return "Woof!"

# Creating an object
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.name)  # Accessing attributes
print(my_dog.bark())  # Calling a method