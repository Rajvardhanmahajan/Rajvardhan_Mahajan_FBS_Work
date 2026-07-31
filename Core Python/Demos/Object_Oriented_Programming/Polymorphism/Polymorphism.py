# Base Class
class Emp:

    # Constructor
    def __init__(self, id, name, sal):
        self.__id = id
        self.__name = name
        self.__sal = sal

    # Getter & Setter for ID
    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    # Getter & Setter for Name
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    # Getter & Setter for Salary
    def getSal(self):
        return self.__sal

    def setSal(self, sal):
        self.__sal = sal

    # Calculate Salary
    def calSal(self):
        print(f"Final Salary = {self.__sal}")

    # Display
    def display(self):
        print(f"ID = {self.getId()}\t"
              f"Name = {self.getName()}\t"
              f"Salary = {self.getSal()}", end="\t")


# Derived Class - HR
class Hr(Emp):

    # Constructor
    def __init__(self, id, name, sal, com):
        super().__init__(id, name, sal)
        self.__com = com

    # Getter & Setter
    def getCom(self):
        return self.__com

    def setCom(self, com):
        self.__com = com

    # Overridden Display Method
    def display(self):
        super().display()
        print(f"Commission = {self.getCom()}")

    # # Overridden Salary Method
    # def calSal(self):
    #     finalSal = self.getSal() + self.getCom()
    #     print(f"Final Salary of HR = {finalSal}")


# Derived Class - Developer
class Dev(Emp):

    # Constructor
    def __init__(self, id, name, sal, incentive):
        super().__init__(id, name, sal)
        self.__incentive = incentive

    # Getter & Setter
    def getIncentive(self):
        return self.__incentive

    def setIncentive(self, incentive):
        self.__incentive = incentive

    # Overridden Display Method
    def display(self):
        super().display()
        print(f"Incentive = {self.getIncentive()}")

    # # Overridden Salary Method
    # def calSal(self):
    #     finalSal = self.getSal() + self.getIncentive()
    #     print(f"Final Salary of Developer = {finalSal}")


# ---------------- Main Program ----------------

e = Emp(102,"Rajesh", 50000)
h = Hr(101, "Rajvardhan", 50000, 5000)
d = Dev(201, "Rohit", 55000, 8000)

# e.display()
# e.calSal()
# print()

# h.display()
h.calSal()
d.calSal()

# print()

# d.display()
# d.calSal()