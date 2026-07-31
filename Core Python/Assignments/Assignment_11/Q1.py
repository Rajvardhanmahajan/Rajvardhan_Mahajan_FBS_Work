#1. Python Program to Put Even and Odd elements of a List into two Different Lists.
# Program to separate even and odd elements into two different lists

# Function to separate even and odd numbers
def separate_even_odd(numbers, even_numbers, odd_numbers):

    # Traverse the original list
    for num in numbers:

        # Check whether the number is even
        if num % 2 == 0:
            even_numbers.append(num)

        # Otherwise, store it in the odd list
        else:
            odd_numbers.append(num)

    # Display the original and separated lists
    print("Original List      :", numbers)
    print("Even Numbers List  :", even_numbers)
    print("Odd Numbers List   :", odd_numbers)


# Main Program

# Original list
numbers = [10, 15, 20, 25, 30, 35]

# Empty lists to store even and odd numbers
even_numbers = []
odd_numbers = []

# Call the function
separate_even_odd(numbers, even_numbers, odd_numbers)