#7. Find the sum of three-digit number.

#Take input 
num = int(input('Enter number: '))

#Perform Operation
d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

sum = d1 + d2 + d3 

#Display result

print('The sum of three digits is =', sum)