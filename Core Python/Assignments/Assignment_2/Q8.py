#8. Write a program to swap two numbers using third variable.

#Take input
x = int(input('Enter Number1: '))
y = int(input('Enter Number2: '))

print('Number Before swapping: =', x, y)
#Perform operation

z = y
y = x
x = z

#Display result
print(f'Number after swapping: {x} and {y}')