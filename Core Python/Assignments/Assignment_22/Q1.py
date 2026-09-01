# Import pickle module to store and retrieve objects
import pickle

# Import os module to work with file paths
import os


# Create Employee class
class Emp:

    # Parameterized constructor
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    # Convert employee object into readable string
    def __str__(self):
        return f"ID = {self.eid}\tName = {self.ename}\tBasic = {self.basic}"


# Create employee.dat file path in the same folder as this Python file
FILE = os.path.join(os.path.dirname(__file__), "employee.dat")


# Function to add a new employee record
def add_record():

    # Accept employee details
    eid = int(input("Enter Employee ID: "))
    ename = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))

    # Create Employee object
    emp = Emp(eid, ename, basic)

    # Open file in append binary mode
    with open(FILE, "ab") as f:

        # Store employee object in file
        pickle.dump(emp, f)

    print("Record added successfully.")


# Function to display all employee records
def display_all():
    try:

        # Open file in read binary mode
        with open(FILE, "rb") as f:
            while True:
                try:

                    # Read employee object from file
                    emp = pickle.load(f)

                    # Display employee details
                    print(emp)

                # End of file
                except EOFError:
                    break

    # Handle file not found error
    except FileNotFoundError:
        print("No records found.")


# Function to search employee record using ID
def search_record():

    # Accept employee ID
    eid = int(input("Enter Employee ID to search: "))
    found = False

    try:

        # Open file in read binary mode
        with open(FILE, "rb") as f:
            while True:
                try:

                    # Read employee object
                    emp = pickle.load(f)

                    # Check employee ID
                    if emp.eid == eid:
                        print("Record Found:")
                        print(emp)
                        found = True
                        break

                # End of file
                except EOFError:
                    break

    # Handle file not found error
    except FileNotFoundError:
        print("No records found.")

    # If employee ID was not found
    if not found:
        print("Record not found.")


# Function to delete employee record
def delete_record():

    # Accept employee ID
    eid = int(input("Enter Employee ID to delete: "))

    # Create empty list to store remaining records
    records = []

    try:

        # Open file in read binary mode
        with open(FILE, "rb") as f:
            while True:
                try:

                    # Read employee object
                    emp = pickle.load(f)

                    # Keep records except the record to delete
                    if emp.eid != eid:
                        records.append(emp)

                # End of file
                except EOFError:
                    break

        # Open file in write binary mode
        with open(FILE, "wb") as f:

            # Store remaining records back into file
            for emp in records:
                pickle.dump(emp, f)

        print("Record deleted successfully.")

    # Handle file not found error
    except FileNotFoundError:
        print("No records found.")


# Function to edit employee record
def edit_record():

    # Accept employee ID
    eid = int(input("Enter Employee ID to edit: "))

    # Create empty list for records
    records = []
    found = False

    try:

        # Open file in read binary mode
        with open(FILE, "rb") as f:
            while True:
                try:

                    # Read employee object
                    emp = pickle.load(f)

                    # Check employee ID
                    if emp.eid == eid:

                        # Accept new employee details
                        emp.ename = input("Enter New Name: ")
                        emp.basic = float(input("Enter New Basic Salary: "))
                        found = True

                    # Add record to list
                    records.append(emp)

                # End of file
                except EOFError:
                    break

        # Rewrite updated records into file
        with open(FILE, "wb") as f:
            for emp in records:
                pickle.dump(emp, f)

        # Display update result
        if found:
            print("Record updated successfully.")
        else:
            print("Record not found.")

    # Handle file not found error
    except FileNotFoundError:
        print("No records found.")


# Menu-driven program
while True:

    # Display menu
    print("\n----- Employee Menu -----")
    print("1. Add Record")
    print("2. Search Record")
    print("3. Delete Record")
    print("4. Edit Record")
    print("5. Display All Records")
    print("6. Exit")

    # Accept user's choice
    choice = int(input("Enter your choice: "))

    # Add employee record
    if choice == 1:
        add_record()

    # Search employee record
    elif choice == 2:
        search_record()

    # Delete employee record
    elif choice == 3:
        delete_record()

    # Edit employee record
    elif choice == 4:
        edit_record()

    # Display all records
    elif choice == 5:
        display_all()

    # Exit the program
    elif choice == 6:
        print("Program Ended.")
        break

    # Handle invalid menu choice
    else:
        print("Invalid choice.")