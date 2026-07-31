# Single Inheritance

class Vehicle:

    def __init__(self, company):
        self.__company = company

    def getCompany(self):
        return self.__company

    def setCompany(self, company):
        self.__company = company

    def display(self):
        print("Company :", self.__company)


class Car(Vehicle):

    def __init__(self, company, model):
        super().__init__(company)
        self.__model = model

    def getModel(self):
        return self.__model

    def setModel(self, model):
        self.__model = model

    def display(self):
        super().display()
        print("Model :", self.__model)


c = Car("Mahindra", "XUV700")
c.display()