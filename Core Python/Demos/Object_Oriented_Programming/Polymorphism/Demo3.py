# Runtime Polymorphism using Hospital Management

# Base Class
class Hospital:

    # Constructor
    def __init__(self, patientName):
        self.__patientName = patientName

    # Getter & Setter
    def getPatientName(self):
        return self.__patientName

    def setPatientName(self, patientName):
        self.__patientName = patientName

    # Display Method
    def display(self):
        print("Patient Name :", self.__patientName)

    # Method to Override
    def work(self):
        print("Hospital Staff Working")


# Derived Class
class Doctor(Hospital):

    # Constructor
    def __init__(self, patientName, specialization):
        super().__init__(patientName)
        self.__specialization = specialization

    # Getter & Setter
    def getSpecialization(self):
        return self.__specialization

    def setSpecialization(self, specialization):
        self.__specialization = specialization

    # Display Method
    def display(self):
        super().display()
        print("Specialization :", self.__specialization)

    # Method Overriding
    def work(self):
        print("Doctor is Treating the Patient")


# Derived Class
class Receptionist(Hospital):

    # Constructor
    def __init__(self, patientName, counterNo):
        super().__init__(patientName)
        self.__counterNo = counterNo

    # Getter & Setter
    def getCounterNo(self):
        return self.__counterNo

    def setCounterNo(self, counterNo):
        self.__counterNo = counterNo

    # Display Method
    def display(self):
        super().display()
        print("Counter No :", self.__counterNo)

    # Method Overriding
    def work(self):
        print("Receptionist is Managing Appointments")


# Driver Code
d = Doctor("Raj", "Cardiology")
d.display()
d.work()

print()

r = Receptionist("Amit", 5)
r.display()
r.work()