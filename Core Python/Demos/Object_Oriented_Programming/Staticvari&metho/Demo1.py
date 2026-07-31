# Static Method Example

class Employee:

    # Static Variable
    company = "Tech Solutions"

    # Constructor
    def __init__(self, empId, empName):
        self.__empId = empId
        self.__empName = empName

    # Static Method
    @staticmethod
    def companyInfo():
        print("Company Name :", Employee.company)
        print("Location : Pune")
        print("Working Days : Monday to Friday")

    # Getter Methods
    def getEmpId(self):
        return self.__empId

    def getEmpName(self):
        return self.__empName

    # Setter Methods
    def setEmpId(self, empId):
        self.__empId = empId

    def setEmpName(self, empName):
        self.__empName = empName

    # Display Method
    def display(self):
        print("Employee ID :", self.__empId)
        print("Employee Name :", self.__empName)


# Driver Code
# Calling Static Method using Class Name
Employee.companyInfo()

print()

e1 = Employee(101, "Raj")
e2 = Employee(102, "Kunal")
e1.display()
e2.display()

