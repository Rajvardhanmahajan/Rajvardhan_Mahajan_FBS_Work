#6. Python Program to Find the Union of two Lists

# Function to find the union of two lists
def find_union(list1, list2, union_list):

    # Add unique elements from the first list
    for num in list1:
        if num not in union_list:
            union_list.append(num)

    # Add unique elements from the second list
    for num in list2:
        if num not in union_list:
            union_list.append(num)

    # Display the union list
    print("Union List :", union_list)


# Main Program

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

union_list = []

# Call the function
find_union(list1, list2, union_list)