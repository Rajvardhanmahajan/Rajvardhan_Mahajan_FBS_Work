#7. Program to Find the Roots of a Quadratic Equation

#Take input
a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))
c = int(input('Enter value of c: '))

#perform operation
d = b ** 2 - (4 * a * c)

r1 = (-b + ( d ** 0.5 )) / (2 * a)

r2 = (-b - ( d ** 0.5 )) / (2 * a)

#Display result
print('Root 1:', r1)
print('Root 2:', r2)