# Multilevel Inheritance Program

# Base Class
class Animal:
    # Constructor
    def __init__(self, name):
        self.__name = name

    #Getter & setter for name
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name

    #Display Method
    def display(self):
        print('Animal name :',self.__name)

#Derived Class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.__breed = breed

    #Getter & setter for breed
    def getbreed(self):
        return self.__breed
    def setbreed(self,breed):
        self.__breed = breed

    #Display method
    def display(self):
        super().display()
        print('Breed :',self.__breed)

#Derived class of Dog
class Puppy(Dog):
    def __init__(self, name, breed, age):
        super().__init__(name, breed)
        self.__age = age

    #Getter & setter for age
    def getAge(self):
        return self.__age
    def setAge(self,age):
        self.__age = age

    #Display method
    def display(self):
        super().display()
        print('Age :', self.__age)

#Object 
p = Puppy('Tommy','Labrador', 1)
p.display()