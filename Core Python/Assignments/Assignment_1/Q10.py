#10. Write a program to calculate area of an equilateral triangle.

# Take input
side = int(input('Enter the Side: '))

#perform operation
Area = int(((3 ** 0.5) / 4) * side * side)

#display result
print(f'Area of equilateral triangle is {Area}.')