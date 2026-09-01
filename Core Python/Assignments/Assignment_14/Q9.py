# 9. Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.

def find_combinations(numbers, target):

    print("Combinations whose sum is", target, ":")

    # Select the first number
    for i in range(len(numbers)):

        # Select the second number after the first
        for j in range(i + 1, len(numbers)):

            # Select the third number after the second
            for k in range(j + 1, len(numbers)):

                # Check whether the sum is equal to target
                if numbers[i] + numbers[j] + numbers[k] == target:

                    print(numbers[i], numbers[j], numbers[k])


# Main Program

numbers = [1, 2, 3, 4, 5, 6]

target = 10

# Call the function
find_combinations(numbers, target)