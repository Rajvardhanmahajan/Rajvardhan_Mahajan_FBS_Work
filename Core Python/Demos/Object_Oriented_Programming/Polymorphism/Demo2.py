# Runtime Polymorphism using Notification System

# Base Class
class Notification:

    # Constructor
    def __init__(self, receiver):
        self.__receiver = receiver

    # Getter & Setter
    def getReceiver(self):
        return self.__receiver

    def setReceiver(self, receiver):
        self.__receiver = receiver

    # Display Method
    def display(self):
        print("Receiver :", self.__receiver)

    # Method to Override
    def send(self):
        print("Notification Sent")


# Derived Class
class Email(Notification):

    # Constructor
    def __init__(self, receiver, email):
        super().__init__(receiver)
        self.__email = email

    # Getter & Setter
    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    # Display Method
    def display(self):
        super().display()
        print("Email :", self.__email)

    # Method Overriding
    def send(self):
        print("Notification Sent through Email")


# Derived Class
class SMS(Notification):

    # Constructor
    def __init__(self, receiver, mobileNo):
        super().__init__(receiver)
        self.__mobileNo = mobileNo

    # Getter & Setter
    def getMobileNo(self):
        return self.__mobileNo

    def setMobileNo(self, mobileNo):
        self.__mobileNo = mobileNo

    # Display Method
    def display(self):
        super().display()
        print("Mobile No :", self.__mobileNo)

    # Method Overriding
    def send(self):
        print("Notification Sent through SMS")


# Driver Code
e = Email("Raj", "raj@gmail.com")
e.display()
e.send()

print()

s = SMS("Amit", "9876543210")
s.display()
s.send()