# 2. Create a derived class from Student as EnggStudent with :
# a. Data members as :
# i. Branch
# ii. InternalMarks
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method

# Import Student class from Q1
from Q1 import Student


# EnggStudent inherits properties and methods from Student
class EnggStudent(Student):

    # Parameterized constructor
    def __init__(self, studentId, name, age, percentage, branch, internalMarks):

        # Call parent class constructor
        super().__init__(studentId, name, age, percentage)

        # Initialize Engineering Student specific members
        self.branch = branch
        self.internalMarks = internalMarks

    # Display Engineering Student details
    def display(self):
        print(self)

    # Accept student details from user
    def accept(self):

        # Call parent class accept() to accept basic student details
        super().accept()

        # Accept Engineering Student specific details
        self.branch = input("Enter Branch: ")
        self.internalMarks = float(input("Enter Internal Marks: "))

    # Calculate rank based on percentage and internal marks
    def calculateRank(self):

        # First Class if percentage >= 75 and internal marks >= 40
        if self.percentage >= 75 and self.internalMarks >= 40:
            return "First Class"

        # Second Class if percentage >= 60
        elif self.percentage >= 60:
            return "Second Class"

        # Otherwise Fail
        else:
            return "Fail"

    # Override __str__ method to display all details
    def __str__(self):
        return (f"StudentId = {self.studentId}\t"
                f"Name = {self.name}\t"
                f"Age = {self.age}\t"
                f"Percentage = {self.percentage}\t"
                f"Branch = {self.branch}\t"
                f"InternalMarks = {self.internalMarks}\t"
                f"Rank = {self.calculateRank()}")


# Create Engineering Student object using parameterized constructor
e1 = EnggStudent(101, "Ashish", 23, 49, "IT", 40)

# Create an empty Engineering Student object
e2 = EnggStudent(0, "", 0, 0, "", 0)

# Accept student details from user
e2.accept()

# Display first student's details
e1.display()

# Display second student's details
e2.display()