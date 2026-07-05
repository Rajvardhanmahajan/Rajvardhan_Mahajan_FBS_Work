#1. Write a program to check if the given number is positive or negative.

#Take input
num = int(input('Enter the number: '))

#Perform operation
if (num > 0):
    print(f'The Number is positive {num}.')
elif (num < 0):
    print(f'The number is negative {num}.')
else:
    print(f'The number is zero.')