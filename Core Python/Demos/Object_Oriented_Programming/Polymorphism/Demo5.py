# Runtime Polymorphism using Authentication System

# Base Class
class Authentication:

    # Constructor
    def __init__(self, userName):
        self.__userName = userName

    # Getter & Setter
    def getUserName(self):
        return self.__userName

    def setUserName(self, userName):
        self.__userName = userName

    # Display Method
    def display(self):
        print("User Name :", self.__userName)

    # Method to Override
    def verify(self):
        print("User Authentication")


# Derived Class
class Fingerprint(Authentication):

    # Constructor
    def __init__(self, userName, fingerID):
        super().__init__(userName)
        self.__fingerID = fingerID

    # Getter & Setter
    def getFingerID(self):
        return self.__fingerID

    def setFingerID(self, fingerID):
        self.__fingerID = fingerID

    # Display Method
    def display(self):
        super().display()
        print("Finger ID :", self.__fingerID)

    # Method Overriding
    def verify(self):
        print("User Verified using Fingerprint")


# Derived Class
class FaceID(Authentication):

    # Constructor
    def __init__(self, userName, faceCode):
        super().__init__(userName)
        self.__faceCode = faceCode

    # Getter & Setter
    def getFaceCode(self):
        return self.__faceCode

    def setFaceCode(self, faceCode):
        self.__faceCode = faceCode

    # Display Method
    def display(self):
        super().display()
        print("Face Code :", self.__faceCode)

    # Method Overriding
    def verify(self):
        print("User Verified using Face ID")


# Driver Code
f = Fingerprint("Raj", "FP101")
f.display()
f.verify()

print()

fa = FaceID("Amit", "FACE202")
fa.display()
fa.verify()