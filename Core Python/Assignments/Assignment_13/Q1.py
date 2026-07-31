#1. Python Program to Add a Key-Value Pair to the Dictionary

# Function to add key-value pairs
def add_key_value(student_dict):

    n = int(input("Enter how many key-value pairs you want to add: "))

    for i in range(n):

        # Accept key and value
        key = input("\nEnter Key   : ")
        value = input("Enter Value : ")

        # Add the key-value pair
        student_dict[key] = value

    # Display the updated dictionary
    print("\nUpdated Dictionary:")

    for key, value in student_dict.items():
        print(key, ":", value)


# Main Program

student_dict = {}

# Call the function
add_key_value(student_dict)