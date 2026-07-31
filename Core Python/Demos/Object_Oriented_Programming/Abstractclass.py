from abc import ABC,abstractmethod
# Base Class
class Emp(ABC):
    # Constructor
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal
    # Getter & setter for ID
    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id
    # Getter & setter for name
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    # Getter & setter for Salary
    def getSal(self):
        return self.sal
    def setSal(self, sal):
        self.sal = sal

    @abstractmethod
    # Display Employee Salary
    def calSal(self):
        #print(f'Emp Salary = {self.sal}')
        pass
    # # Display Employee Details
    # def display(self):
    #     print(f'ID = {self.id}\tName = {self.name}\tSalary = {self.sal}', end='\t')

# Derived Class - HR
class Hr(Emp):
    # Constructor
    def __init__(self, id, name, sal, com):
        super().__init__(id, name, sal)
        self.com = com

    # Getter Method for Commission
    def getCom(self):
        return self.com

    # Setter Method for Commission
    def setcom(self, com):
        self.com = com

    def calSal(self):
        finalsal = self.getSal()+self.com
        print(f"Salary: {finalsal}")


# Creating an object of HR class
h1 = Hr(301, "Smriti", 60000, 10000)

# Creating objects of Employee class
# e1 = Emp(101, "Rajvardhan", 45000)
# e2 = Emp(102, "Tanuja", 38000)
# e3 = Emp(103, "Vidya", 42000)
# Displaying Details
# h1.display()
# de1.display()
h1.calSal()


    
