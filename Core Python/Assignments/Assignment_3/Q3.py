#3. Write a program to input angles of a triangle and check whether triangle is valid or not.

#Take input
#Taking Angles /_a, /_b, /_c.

a = int(input('Enter first Angle: '))
b = int(input('Enter second Angle: '))
c = int(input('Enter third Angle: '))

#Perform operation
sum = a + b + c

# if (sum == 180):
if (a + b + c == 180):
    print('The triangle is valid.')
else:
    print('The triangle is invalid.')
