# 6. Python Program to Multiply All the Items in a Dictionary

# Function to multiply all values
def multiply_items(table_dict):

    product = 1

    # Traverse the dictionary
    for key in table_dict:

        # Multiply each value
        product *= table_dict[key]

    # Display the result
    print("Dictionary :", table_dict)
    print("Product of Values :", product)


# Main Program

table_dict = {
    "1": 2,
    "2": 4,
    "3": 6,
    "4": 8,
    "5": 10
}

# Call the function
multiply_items(table_dict)
