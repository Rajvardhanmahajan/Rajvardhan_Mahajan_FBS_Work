# from abc import ABC,abstractmethod
# class Veichal(ABC):
#     def __init__(self,name,color,price):
#         self.__name=name
#         self.__price=price
#         self.__color=color
#     @abstractmethod
#     def brake(self):
#         pass
#     def __str__(self):
#         return f"Name= {self.__name} \t Price={self.__price}\tColor={self.__color}"
# class Car(Veichal):
#     def __init__(self, name, color, price,sBEalt):
#         super().__init__(name, color, price)
#         self.__seatBelt=sBEalt
#     def brake(self):
#         print("This is the Drump break of Car ")
#     def __str__(self):
#         return super().__str__() + f"\tSeat Belt={self.__seatBelt}"
# v=Car("BMW","Black",1200000,6)
# v.brake()
# print(v)


#Animal
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,color, bride):
        self.__color = color
        self.__bride = bride

    def getColor(self):
        return self.__color
    def setColor(self,color):
        self.__color = color

    def getBride(self):
        return self.__bride
    def setBride(self,bride):
        self.__bride = bride

    @abstractmethod
    def sound(self):
        pass

    def __str__(self):
        return f"Color = {self.__color}\t Bride = {self.__bride}"

class Dog(Animal):
    def __init__(self, color, bride, year):
        super().__init__(color, bride)
        self.__year = year

    def sound(self):
        print("Bark")

    def __str__(self):
        return super().__str__() + f"\t Year = {self.__year}"

d = Dog("Black","Labra",5)
d.sound()
print(d)