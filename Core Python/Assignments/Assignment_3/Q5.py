#5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

#Take inputs Three sides x, y , z 

x = int(input('Enter first side: '))
y = int(input('Enter second side: '))
z = int(input('Enter third side: '))

#Perform operation
if (x == y and y == z and z == x):
    print('The triangle is equilateral.')
elif (x == y or y == z or z == x):
    print('The triangle is isoscele.')
else:
    print('The triangle is scalene.')