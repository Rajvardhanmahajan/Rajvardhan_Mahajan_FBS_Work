# 5. Python Program to Sum All the Items in a Dictionary

# Function to calculate the sum of values
def sum_of_items(student_dict):

    total = 0

    # Traverse the dictionary
    for key in student_dict:

        # Add each value to the total
        total += student_dict[key]

    # Display the result
    print("Dictionary :", student_dict)
    print("Sum of Values :", total)


# Main Program

student_dict = {
    "Math": 80,
    "Science": 75,
    "English": 90
}

# Call the function
sum_of_items(student_dict)