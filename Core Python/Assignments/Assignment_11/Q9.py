#9. Write a program to create three lists of numbers, their squares and cubes

#Function to find square and cube list
def squares_cube(numbers, square_li, cube_li):
    
    #loop for square list
    for num in numbers:
        square_li.append(num ** 2)

    #loop for cube list
    for num in numbers:
        cube_li.append(num ** 3)

    print('Original List  :', numbers)
    print('\nSqure List     :', square_li)
    print('Cube List      :', cube_li)


#Main program
numbers = [2, 3, 4, 5, 6, 7, 8]

square_li = []
cube_li = []

squares_cube(numbers, square_li, cube_li)