#9. Write a program to swap two numbers without using third variable.

#Take input
x = int(input('Enter The Number1: '))
y = int(input('Enter The Number2: '))

print(f'The number before swapping: x ={x} y ={y}')
#Perform operation
x = x + y
y = x - y
x = x - y 

#Display result
print(f'The numbers After swapping: x ={x} y ={y}')