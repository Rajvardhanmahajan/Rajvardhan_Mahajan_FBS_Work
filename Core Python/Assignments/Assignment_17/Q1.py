# 1. Create a class Student with following
# a. data members :
# i. StudentId
# ii. Name
# iii. Age
# iv. Percentage
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. Method CalculateRank
# v. Override __str__ Method


# Create Student class
class Student:

    # Parameterized constructor
    def __init__(self, studentId, name, age, percentage):
        # Initialize student data members
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    # Display student details
    def display(self):
        print(self)

    # Accept student details from user
    def accept(self):
        self.studentId = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    # Calculate student's rank/class based on percentage
    def calculateRank(self):
        if self.percentage >= 75:
            return "First Class"

        elif self.percentage >= 60:
            return "Second Class"

        elif self.percentage >= 50:
            return "Third Class"

        else:
            return "Fail"

    # Override __str__ method to display student details
    def __str__(self):
        return f"StudentId = {self.studentId}\tName = {self.name}\tAge = {self.age}\tPercentage = {self.percentage}\tRank = {self.calculateRank()}"


# Create Student object using parameterized constructor
# s1 = Student(101, "Raj", 23, 82.5)

# Create empty/default Student object
# s2 = Student(0, "", 0, 0)

# Accept student details from user
# s2.accept()

# Display first student's details
# s1.display()

# Display second student's details
# s2.display()