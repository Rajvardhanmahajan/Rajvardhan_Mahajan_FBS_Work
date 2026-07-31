# Single Inheritance Program

# Base Class
class Animal:

    # Constructor
    def __init__(self, name):
        self.name = name

    # Display Method
    def display(self):
        print("Animal Name :", self.name)


# Derived Class
class Dog(Animal):

    # Constructor
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    # Display Method
    def display(self):
        super().display()
        print("Breed :", self.breed)


# Driver Code
d = Dog("Tommy", "Labrador")
d.display()