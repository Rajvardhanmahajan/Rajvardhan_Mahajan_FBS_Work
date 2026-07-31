#11. Write a program to print all numbers which are divisible by m and n in the list.

# Function to find divisible numbers
def find_divisible_numbers(numbers, m, n, divisible_numbers):

    # Traverse the original list
    for num in numbers:

        # Check if the number is divisible by both m and n
        if num % m == 0 and num % n == 0:
            divisible_numbers.append(num)

    # Display the result
    print("Numbers divisible by", m, "and", n, ":", divisible_numbers)


# Main Program

# Original list
numbers = [10, 20, 30, 40, 50, 60]

# Divisors
m = 2
n = 5

# Empty list to store divisible numbers
divisible_numbers = []

# Call the function
find_divisible_numbers(numbers, m, n, divisible_numbers)
