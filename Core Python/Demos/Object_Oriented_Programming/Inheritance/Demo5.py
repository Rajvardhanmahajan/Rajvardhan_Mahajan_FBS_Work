# Multilevel Inheritance

# Base Class
class Bank:

    # Constructor
    def __init__(self, bankName):
        self.__bankName = bankName

    # Getter & Setter
    def getBankName(self):
        return self.__bankName

    def setBankName(self, bankName):
        self.__bankName = bankName

    # Display Method
    def display(self):
        print("Bank Name :", self.__bankName)


# Derived Class
class Account(Bank):

    # Constructor
    def __init__(self, bankName, accountNo):
        super().__init__(bankName)
        self.__accountNo = accountNo

    # Getter & Setter
    def getAccountNo(self):
        return self.__accountNo

    def setAccountNo(self, accountNo):
        self.__accountNo = accountNo

    # Display Method
    def display(self):
        super().display()
        print("Account No :", self.__accountNo)


# Derived Class of Account
class SavingsAccount(Account):

    # Constructor
    def __init__(self, bankName, accountNo, balance):
        super().__init__(bankName, accountNo)
        self.__balance = balance

    # Getter & Setter
    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        self.__balance = balance

    # Display Method
    def display(self):
        super().display()
        print("Balance :", self.__balance)


# Driver Code
s = SavingsAccount("SBI", 123456789, 50000)
s.display()