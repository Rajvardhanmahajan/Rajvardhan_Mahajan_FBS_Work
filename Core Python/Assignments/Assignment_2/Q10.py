#10. Write a program to reverse three-digit number.

num = int(input('Enter the three digit number: '))

print(f'The Original value is: {num}.')
#Perform operation

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

rev = (d1 * 100) + (d2 * 10) + (d3)

#Display result
print(f'The reverse no is {rev}.')