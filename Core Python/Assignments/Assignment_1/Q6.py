#6. Write a Program to input two angles from user and find third angle of the triangle.

# Take input
angle1 = int(input('Enter the angle1: '))
angle2 = int(input('Enter the angle2: '))

#perform operation
angle3 = 180 - (angle1 + angle2)

#Display result
print(f'The angle1 is {angle1} and angle2 is {angle2} and after find angle3 is {angle3}.')