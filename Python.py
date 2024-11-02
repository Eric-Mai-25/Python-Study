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