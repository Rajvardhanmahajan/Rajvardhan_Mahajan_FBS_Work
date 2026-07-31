# Runtime Polymorphism using Employee Management

# Base Class
class Employee:

    # Constructor
    def __init__(self, empName):
        self.__empName = empName

    # Getter & Setter
    def getEmpName(self):
        return self.__empName

    def setEmpName(self, empName):
        self.__empName = empName

    # Display Method
    def display(self):
        print("Employee Name :", self.__empName)

    # Method to Override
    def work(self):
        print("Employee is Working")


# Derived Class
class HR(Employee):

    # Constructor
    def __init__(self, empName, department):
        super().__init__(empName)
        self.__department = department

    # Getter & Setter
    def getDepartment(self):
        return self.__department

    def setDepartment(self, department):
        self.__department = department

    # Display Method
    def display(self):
        super().display()
        print("Department :", self.__department)

    # Method Overriding
    def work(self):
        print("HR is Recruiting Employees")


# Derived Class
class Developer(Employee):

    # Constructor
    def __init__(self, empName, language):
        super().__init__(empName)
        self.__language = language

    # Getter & Setter
    def getLanguage(self):
        return self.__language

    def setLanguage(self, language):
        self.__language = language

    # Display Method
    def display(self):
        super().display()
        print("Programming Language :", self.__language)

    # Method Overriding
    def work(self):
        print("Developer is Writing Code")


# Driver Code
h = HR("Raj", "Human Resource")
h.display()
h.work()

print()

d = Developer("Amit", "Python")
d.display()
d.work()