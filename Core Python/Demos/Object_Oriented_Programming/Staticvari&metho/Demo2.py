# Static Method Example using Bank

class Bank:

    # Constructor
    def __init__(self, accNo, accHolder):
        self.__accNo = accNo
        self.__accHolder = accHolder

    # Getter Methods
    def getAccNo(self):
        return self.__accNo

    def getAccHolder(self):
        return self.__accHolder

    # Setter Methods
    def setAccNo(self, accNo):
        self.__accNo = accNo

    def setAccHolder(self, accHolder):
        self.__accHolder = accHolder

    # Display Method
    def display(self):
        print("Account Number :", self.__accNo)
        print("Account Holder :", self.__accHolder)

    # Static Method
    @staticmethod
    def calculateInterest(principal, rate, time):
        interest = (principal * rate * time) / 100
        print("Simple Interest :", interest)


# Driver Code
b = Bank(101, "Raj")
b.display()

print()

Bank.calculateInterest(50000, 8, 2)