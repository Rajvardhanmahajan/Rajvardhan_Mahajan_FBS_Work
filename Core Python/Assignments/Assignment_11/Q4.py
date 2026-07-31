#4. Python Program to Find the Second Largest Number in a List Using Bubble Sort.

# Function to sort the list using Bubble Sort
def bubble_sort(numbers):

    size = len(numbers)

    # Bubble Sort
    for i in range(1, size-1):
        for j in range(0, size -i):

            # Swap if the current element is greater
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


# Function to find the second largest element
def find_second_largest(numbers):

    # Sort the list
    bubble_sort(numbers)

    # Display the sorted list
    print("Sorted List           :", numbers)

    # Display the second largest element
    print("Second Largest Number :", numbers[-2])


# Main Program

numbers = [30, 10, 50, 20, 40]

print("Original List         :", numbers)

find_second_largest(numbers)