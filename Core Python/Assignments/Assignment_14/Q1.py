# 1. Write a Python program to find elements in a given set that are not in another set.# Program to find elements present in the first set but not in the second set

# Function to find the difference of two sets
def set_difference(set1, set2):

    result = set()
 
    # Traverse the first set
    for element in set1:

        # Check whether the element is not present in the second set
        if element not in set2:
            result.add(element)

    # Display the result
    print("Set 1 :", set1)
    print("Set 2 :", set2)
    print("Elements present only in Set 1 :", result)


# Main Program

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 60}

# Call the function
set_difference(set1, set2)