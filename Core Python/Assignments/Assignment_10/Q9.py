#9. Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

# Function to create a list
def create_list(numbers):

    count = int(input("Enter the number of elements: "))

    for i in range(count):
        element = int(input("Enter element: "))
        numbers.append(element)


# Function to separate even and odd numbers
def separate_even_odd(numbers, even_numbers, odd_numbers):

    for num in numbers:

        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    print("\nEven Numbers :", even_numbers)
    print("Odd Numbers  :", odd_numbers)


# Main Program

numbers = []

create_list(numbers)

print("\nOriginal List :", numbers)

even_numbers = []
odd_numbers = []

separate_even_odd(numbers, even_numbers, odd_numbers)