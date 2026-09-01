# Import SYMARKS class from SY package
from SY.symarks import SYMARKS

# Import TYMarks class from TY package
from TY.tymarks import TYMarks


# Create Student class
class Student:

    # Parameterized constructor
    def __init__(self, rollNo, name, syMarks, tyMarks):
        self.rollNo = rollNo
        self.name = name
        self.syMarks = syMarks
        self.tyMarks = tyMarks

    # Calculate grade based on percentage
    def calculateGrade(self):

        # Calculate total marks
        total = self.syMarks.computer + self.tyMarks.theory

        # Calculate percentage
        percentage = (total / 200) * 100

        # Check percentage and return grade
        if percentage >= 70:
            return "A"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C"
        elif percentage >= 40:
            return "Pass Class"
        else:
            return "Fail"

    # Display student details
    def display(self):

        # Calculate total marks
        total = self.syMarks.computer + self.tyMarks.theory

        print("Roll No =", self.rollNo)
        print("Name =", self.name)
        print("SY Computer =", self.syMarks.computer)
        print("TY Computer =", self.tyMarks.theory)
        print("Total =", total)

        # Call calculateGrade() to display grade
        print("Grade =", self.calculateGrade())


# Create SY marks object
sy = SYMARKS(80, 70, 75)

# Create TY marks object
ty = TYMarks(60, 70)

# Create Student object
s = Student(101, "Raj", sy, ty)

# Display student details and grade
s.display()