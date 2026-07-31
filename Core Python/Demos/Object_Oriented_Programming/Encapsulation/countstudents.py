# Base Class
class Student:

    # Static (Class) Variable
    # Counts the total number of Student objects created
    countstudent = 0

    # Constructor
    def __init__(self, rollNo, name, marks):
        self.rollno = rollNo
        self.name = name
        self.marks = marks

        # Increment the object counter
        Student.countstudent += 1

    # Getter Method for Roll Number
    def getRollNo(self):
        return self.rollno

    # Setter Method for Roll Number
    def setRollNo(self, rollNo):
        self.rollno = rollNo

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

    # Display Student Details
    def display(self):
        print(f"Roll No = {self.rollno}\tName = {self.name}\tMarks = {self.marks}")


# Derived Class
class PlacedStudent(Student):

    # Constructor
    def __init__(self, rollNo, name, marks, sal):
        super().__init__(rollNo, name, marks)
        self.sal = sal

    # Getter Method for Salary
    def getSal(self):
        return self.sal

    # Setter Method for Salary
    def setSal(self, sal):
        self.sal = sal

    # Overridden Display Method
    def display(self):
        super().display()
        return print(f"Salary = {self.sal}")


# ---------------- Main Program ----------------

# Creating Student Objects
s1 = Student(101, "Raj", 86)
s2 = Student(102, "Sachin", 58)

# Creating Placed Student Object
s3 = PlacedStudent(103, "Harsh", 76, 46656)

# Display Total Number of Student Objects
print("Total Students =", Student.countstudent)

# Display Student Details
s1.display()
s2.display()

# Display Placed Student Details
# s3.display()