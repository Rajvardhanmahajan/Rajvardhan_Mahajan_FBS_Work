# 2. Write a Python program to remove the intersection of a second set with a first set.# Program to remove the intersection of the second set from the first set

# Function to remove common elements
def remove_intersection(set1, set2):

    result = set()

    # Traverse the first set
    for element in set1:

        # Add only non-common elements
        if element not in set2:
            result.add(element)

    # Display the result
    print("First Set  :", set1)
    print("Second Set :", set2)
    print("After Removing Common Elements :", result)


# Main Program

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 60}

# Call the function
remove_intersection(set1, set2)