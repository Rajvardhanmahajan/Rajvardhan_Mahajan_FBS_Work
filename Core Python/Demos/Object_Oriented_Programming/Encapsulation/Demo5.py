# Bank Management using Encapsulation

class Bank:

    # Constructor
    def __init__(self, accountNo, name, balance):
        self.__accountNo = accountNo
        self.__name = name
        self.__balance = balance

    # Getter & setter for accountNo
    def getAccountNo(self):
        return self.__accountNo
    def setAccountNo(self, accountNo):
        self.__accountNo = accountNo

    #Getter & setter for Name
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name

    #Getter & setter for balance
    def getBalance(self):
        return self.__balance
    def setBalance(self, balance):
        self.__balance = balance

    # Display Method
    def display(self):
        print("Account No :", self.__accountNo)
        print("Account Holder :", self.__name)
        print("Balance :", self.__balance)

#Class ends..

# Objects
b = Bank(123456789, "Rajvardhan", 50000)

print("Before Update")
b.display()

# Updating Balance using Setter
b.setBalance(75000)

print("\nAfter Update")
b.display()