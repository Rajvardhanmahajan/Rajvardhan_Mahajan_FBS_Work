#12. Write a program to create three lists of numbers, their squares and cubes.

# Function to create square and cube lists
def create_square_cube_lists(numbers, square_list, cube_list):

    # Traverse the original list
    for num in numbers:

        # Store the square of each number
        square_list.append(num ** 2)

        # Store the cube of each number
        cube_list.append(num ** 3)

    # Display all three lists
    print("Original Numbers :", numbers)
    print("Square List      :", square_list)
    print("Cube List        :", cube_list)


# Main Program

# Original list
numbers = [2, 3, 4, 5, 6, 7, 8]

# Empty lists
square_list = []
cube_list = []

# Call the function
create_square_cube_lists(numbers, square_list, cube_list)