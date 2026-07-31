#3. Python Program to Sort the List According to the Second Element in Sublist.

# Function to sort the nested list
def sort_by_second_element(student_records):

    size = len(student_records)

    # Traverse the nested list
    for i in range(size - 1):

        # Assume the current index has the minimum second element
        min_index = i

        # Compare the second element of remaining sublists
        for j in range(i + 1, size):

            if student_records[min_index][1] > student_records[j][1]:
                min_index = j

        # Swap the complete sublists
        student_records[i], student_records[min_index] = student_records[min_index], student_records[i]

    # Display the sorted nested list
    print("\n" \
    "Sorted List :", student_records)


# Main Program

student_records = [[101, 85],[102, 76],[103, 90],[104, 82]]

print("Original List:", student_records)

# Call the function
sort_by_second_element(student_records)
