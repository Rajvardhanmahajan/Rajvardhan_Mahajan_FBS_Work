# 3. Create a class MedicalStudent inherited from Student with following
# :

# i. Data members :Specialization
# ii. MarksOfInternship
# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method

# Import Student class from Q1
from Q1 import Student


# MedicalStudent inherits from Student class
class MedicalStudent(Student):

    # Parameterized constructor
    def __init__(self, studentId, name, age, percentage,
                 specialization, marksOfInternship):

        # Call parent class constructor
        super().__init__(studentId, name, age, percentage)

        # Initialize Medical Student specific members
        self.specialization = specialization
        self.marksOfInternship = marksOfInternship

    # Display Medical Student details
    def display(self):
        print(self)

    # Accept student details from user
    def accept(self):

        # Call parent class accept() method
        super().accept()

        # Accept Medical Student specific details
        self.specialization = input("Enter Specialization: ")
        self.marksOfInternship = float(input("Enter Internship Marks: "))

    # Calculate rank based on percentage and internship marks
    def calculateRank(self):

        # First Class if percentage >= 75 and internship marks >= 40
        if self.percentage >= 75 and self.marksOfInternship >= 40:
            return "First Class"

        # Second Class if percentage >= 60
        elif self.percentage >= 60:
            return "second Class"

        # Otherwise Fail
        else:
            return "Fail"

    # Override __str__ method to display all details
    def __str__(self):
        return (f"StudentId = {self.studentId}\t"
                f"Name = {self.name}\t"
                f"Age = {self.age}\t"
                f"Percentage = {self.percentage}\t"
                f"Specialization = {self.specialization}\t"
                f"InternshipMarks = {self.marksOfInternship}\t"
                f"Rank = {self.calculateRank()}")


# Create Medical Student object using parameterized constructor
m1 = MedicalStudent(103, "Hanmant", 24, 83, "Cardiology", 45)

# Create empty Medical Student object
m2 = MedicalStudent(0, "", 0, 0, "", 0)

# Accept Medical Student details from user
m2.accept()

# Display first student's details
m1.display()

# Display second student's details
m2.display()