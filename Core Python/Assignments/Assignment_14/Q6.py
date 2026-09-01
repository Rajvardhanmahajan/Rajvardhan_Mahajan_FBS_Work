# 6. Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.

# Function to find the maximum product pair
def maximum_product_pair(numbers):

    # Remove duplicate elements
    unique_numbers = list(set(numbers))

    max_product = unique_numbers[0] * unique_numbers[1]
    first_number = unique_numbers[0]
    second_number = unique_numbers[1]

    # Compare every possible pair
    for i in range(len(unique_numbers)):

        for j in range(i + 1, len(unique_numbers)):

            product = unique_numbers[i] * unique_numbers[j]

            if product > max_product:
                max_product = product
                first_number = unique_numbers[i]
                second_number = unique_numbers[j]

    # Display the result
    print("Unique Numbers :", unique_numbers)
    print("Maximum Product Pair :", first_number, second_number)
    print("Maximum Product :", max_product)


# Main Program

numbers = [2, 5, 7, 8, 3, 8, 5]

maximum_product_pair(numbers)