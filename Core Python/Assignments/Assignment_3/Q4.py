#4. Write a program to input all sides of a triangle and check whether triangle is valid or not.

#Take inputs Three sides x, y , z 

x = int(input('Enter first side: '))
y = int(input('Enter second side: '))
z = int(input('Enter third side: '))

#Operation perform
if (x + y > z and y + z > x and x + z > y):
    print('The triangle is valid.')
else:
    print('The triangle is invalid.')