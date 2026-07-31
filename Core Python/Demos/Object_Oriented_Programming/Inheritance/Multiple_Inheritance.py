# Multiple Inheritance Program

# Base Class 1
class Mec:

    # Constructor
    def __init__(self, workshop):
        self.workshop = workshop

    # Display Method
    def display(self):
        print("I am from Mec")


# Base Class 2
class Ent:

    # Constructor
    def __init__(self, lab):
        self.lab = lab

    # Display Method
    def display(self):
        print("I am from Ent")


# Derived Class (Inheriting from Mec and Ent)
class Mechatronics(Mec, Ent):

    # Constructor
    def __init__(self, workshop):
        super().__init__(workshop)


# Driver Code
m = Mechatronics("yes")

# Calling Display Method
m.display()