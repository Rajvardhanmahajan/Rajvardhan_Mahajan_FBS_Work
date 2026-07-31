#13 . Write a program to print list after removing even numbers.

# Function to remove even numbers
def remove_even_numbers(numbers, odd_numbers):

    # Traverse the original list
    for num in numbers:

        # Store only odd numbers
        if num % 2 != 0:
            odd_numbers.append(num)

    # Display the result
    print("Original List             :", numbers)
    print("List After Removing Evens :", odd_numbers)


# Main Program

numbers = [2, 3, 4, 5, 6, 7, 8]

odd_numbers = []

remove_even_numbers(numbers, odd_numbers)