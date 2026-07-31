#5. Python Program to Sort a List According to the Length of the Elements within the list.

# Function to sort the list based on the length of each string
def sort_by_length(words):

    size = len(words)

    # Bubble Sort
    for i in range(size - 1):
        for j in range(size - 1 - i):

            # Compare the length of adjacent strings
            if len(words[j]) > len(words[j + 1]):

                # Swap the strings
                words[j], words[j + 1] = words[j + 1], words[j]

    # Display the sorted list
    print("List Sorted by Length :", words)


# Main Program

words = ["Apple", "Cat", "Elephant", "Bat", "Dog", "Orange"]

print("Original List         :", words)

# Call the function
sort_by_length(words)

