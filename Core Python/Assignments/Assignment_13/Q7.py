# 7. Python Program to Remove the Given Key from a Dictionary


# Function to remove a key
def remove_given_key(student_dict):

    # Accept the key from the user
    search_key = input("Enter the key to remove: ")

    # Check whether the key exists
    if search_key in student_dict:

        # Remove the key
        student_dict.pop(search_key)

        print("\nKey removed successfully.")
        print("Updated Dictionary:", student_dict)

    else:
        print("\nKey not found.")


# Main Program

student_dict = {
    "Name": "Rajvardhan",
    "Class": "FBS",
    "Age": 23,
    "Mo_No": 8010
}

# Call the function
remove_given_key(student_dict)