# Class Definition
class Student:

    # Class (Static) Variable
    # Shared by all objects of the Student class
    collegeName = 'Firstbit Solutions'

    # Constructor
    # Initializes object data when an object is created
    def __init__(self, rollNo, name, marks):
        self.rollno = rollNo
        self.name = name
        self.marks = marks

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
    # Displays the student's details
    def display(self):
        print(f"Roll_no = {self.rollno} \t Name = {self.name} \t Marks = {self.marks}")


# ---------------- Main Program ----------------

# Creating the first Student object
e1 = Student(101, 'Raj', 86)

# Creating the second Student object
e2 = Student(102, 'Sachin', 58)

# Accessing the class variable using the class name
# Student.collegeName

# To print the class variable
print(Student.collegeName)

# Accessing the class variable using an object / Legal, but not preferred. 
# print(e1.collegeName)

# Displaying details of the first student
e1.display()

# Displaying details of the second student
e2.display()