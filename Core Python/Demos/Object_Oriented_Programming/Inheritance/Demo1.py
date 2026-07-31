# Single Inheritance

class Animal:

    # Constructor
    def __init__(self, name):
        self.__name = name

    # Getter & Setter
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    # Display Method
    def display(self):
        print("Animal Name :", self.__name)


class Dog(Animal):

    # Constructor
    def __init__(self, name, breed):
        super().__init__(name)
        self.__breed = breed

    # Getter & Setter
    def getBreed(self):
        return self.__breed

    def setBreed(self, breed):
        self.__breed = breed

    # Display Method
    def display(self):
        super().display()
        print("Breed :", self.__breed)


d = Dog("Tommy", "Labrador")
d.display()