# Single Inheritance

class Employee:

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def display(self):
        print("Employee :", self.__name)


class Manager(Employee):

    def __init__(self, name, department):
        super().__init__(name)
        self.__department = department

    def getDepartment(self):
        return self.__department

    def setDepartment(self, department):
        self.__department = department

    def display(self):
        super().display()
        print("Department :", self.__department)


m = Manager("Raj", "HR")
m.display()
