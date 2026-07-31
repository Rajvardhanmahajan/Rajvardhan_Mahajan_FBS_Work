# Base Class
class Emp:

    # Constructor
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    # Getter Method for ID
    def getId(self):
        return self.id

    # Setter Method for ID
    def setId(self, id):
        self.id = id

    # Getter Method for Name
    def getName(self):
        return self.name

    # Setter Method for Name
    def setName(self, name):
        self.name = name

    # Getter Method for Salary
    def getSal(self):
        return self.sal

    # Setter Method for Salary
    def setSal(self, sal):
        self.sal = sal

    # Display Employee Salary
    def calSal(self):
        print(f'Emp Salary = {self.sal}')

    # Display Employee Details
    def display(self):
        print(f'ID = {self.id}\tName = {self.name}\tSalary = {self.sal}', end='\t')


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

    # Overridden Display Method
    def display(self):
        super().display()
        print(f"Commission = {self.com}")


# Derived Class - Developer
class Dev(Emp):

    # Constructor
    def __init__(self, id, name, sal, incentive):
        super().__init__(id, name, sal)
        self.incentive = incentive

    # Getter Method for Incentive
    def getIncentive(self):
        return self.incentive

    # Setter Method for Incentive
    def setIncentive(self, incentive):
        self.incentive = incentive

    # Overridden Display Method
    def display(self):
        super().display()
        print(f"Incentive = {self.incentive}")


# ---------------- Main Program ----------------

# Creating Developer Object
# Creating an object of Developer class
de1 = Dev(201, "Rohit", 55000, 8000)

# Creating an object of HR class
h1 = Hr(301, "Smriti", 60000, 10000)

# Creating objects of Employee class
e1 = Emp(101, "Rajvardhan", 45000)
e2 = Emp(102, "Tanuja", 38000)
e3 = Emp(103, "Vidya", 42000)
# Displaying Details
h1.display()
de1.display()