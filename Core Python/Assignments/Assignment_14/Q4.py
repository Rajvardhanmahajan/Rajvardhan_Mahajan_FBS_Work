# 4. Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.

# Program to find all pairs whose sum is equal to a given value

# Function to find pairs
def find_pairs(numbers, target):

    print("Pairs whose sum is", target, ":")

    # Compare every element with the remaining elements
    for i in range(len(numbers)):

        for j in range(i + 1, len(numbers)):

            # Check the sum
            if numbers[i] + numbers[j] == target:
                print("(", numbers[i], ",", numbers[j], ")")


# Main Program

numbers = [2, 4, 3, 5, 7, 8, 9]

target = 7

# Call the function
find_pairs(numbers, target)