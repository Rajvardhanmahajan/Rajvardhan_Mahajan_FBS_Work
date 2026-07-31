# Class Definition
class Student:

    # Static (Class) Variable
    # Shared by all objects of the class
    collegeName = "FBS"

    # Constructor
    # Automatically called when an object is created
    def __init__(self, rollNo, name, marks):
        self.rollno = rollNo
        self.name = name
        self.marks = marks

    # Static Method
    # Used to access class (static) variables
    @staticmethod
    def showCollege():
        print("College Name =", Student.collegeName)

    # Getter Method for Roll Number
    def getrollno(self):
        return self.rollno

    # Setter Method for Roll Number
    def setrollno(self, rollno):
        self.rollno = rollno

    # Getter Method for Name
    def getName(self):
        return self.name

    # Setter Method for Name
    def setName(self, name):
        self.name = name

    # Getter Method for Marks
    def getMarks(self):
        return self.marks

    # Setter Method for Marks
    def setMarks(self, marks):
        self.marks = marks

    # Display Method
    # Prints the student's details
    def display(self):
        print(f"Roll No = {self.rollno}\tName = {self.name}\tMarks = {self.marks}")


# ---------------- Main Program ----------------

# Creating the first Student object
s1 = Student(101, "Raj", 86)

# Creating the second Student object
s2 = Student(102, "Sachin", 58)

# Calling the static method using the class name
Student.showCollege()

# Displaying details of the first student
s1.display()

# Displaying details of the second student
s2.display()