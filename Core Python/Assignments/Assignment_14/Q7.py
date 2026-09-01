# 7. Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.

# Function to find missing elements
def find_missing_numbers(set1, set2):

    missing_in_set2 = set()
    missing_in_set1 = set()

    # Elements present in set1 but missing in set2
    for element in set1:
        if element not in set2:
            missing_in_set2.add(element)

    # Elements present in set2 but missing in set1
    for element in set2:
        if element not in set1:
            missing_in_set1.add(element)

    # Display the result
    print("Set 1 :", set1)
    print("Set 2 :", set2)
    print("Missing in Set 2 :", missing_in_set2)
    print("Missing in Set 1 :", missing_in_set1)


# Main Program

set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 5, 6}

# Call the function
find_missing_numbers(set1, set2)