# Runtime Polymorphism using Payment System

# Base Class
class Payment:

    # Constructor
    def __init__(self, customerName):
        self.__customerName = customerName

    # Getter & Setter
    def getCustomerName(self):
        return self.__customerName

    def setCustomerName(self, customerName):
        self.__customerName = customerName

    # Display Method
    def display(self):
        print("Customer Name :", self.__customerName)

    # Method to Override
    def pay(self):
        print("Payment Processing...")


# Derived Class
class UPI(Payment):

    # Constructor
    def __init__(self, customerName, upiId):
        super().__init__(customerName)
        self.__upiId = upiId

    # Getter & Setter
    def getUpiId(self):
        return self.__upiId

    def setUpiId(self, upiId):
        self.__upiId = upiId

    # Display Method
    def display(self):
        super().display()
        print("UPI ID :", self.__upiId)

    # Method Overriding
    def pay(self):
        print("Payment Done using UPI")


# Derived Class
class CreditCard(Payment):

    # Constructor
    def __init__(self, customerName, cardNo):
        super().__init__(customerName)
        self.__cardNo = cardNo

    # Getter & Setter
    def getCardNo(self):
        return self.__cardNo

    def setCardNo(self, cardNo):
        self.__cardNo = cardNo

    # Display Method
    def display(self):
        super().display()
        print("Card Number :", self.__cardNo)

    # Method Overriding
    def pay(self):
        print("Payment Done using Credit Card")


# Driver Code
u = UPI("Raj", "raj@oksbi")
u.display()
u.pay()

print()

c = CreditCard("Amit", "1234-5678-9876")
c.display()
c.pay()