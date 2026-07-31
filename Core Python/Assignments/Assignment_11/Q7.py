#7. Python Program to Find the Intersection of Two Lists

# Function to find the intersection of two lists
def find_intersection(list1, list2, intersection_list):

    # Traverse the first list
    for num in list1:

        # Check if the element is present in both lists
        if num in list2 and num not in intersection_list:
            intersection_list.append(num)

    # Display the intersection list
    print("Intersection List :", intersection_list)


# Main Program

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

intersection_list = []

# Call the function
find_intersection(list1, list2, intersection_list)