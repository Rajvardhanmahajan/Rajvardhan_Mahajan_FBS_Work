#7. Write a program to find sum of digits of a number.

def addition(num):      #Function Defination

    total = 0

    #Peform operation
    while num > 0:

        d = num % 10
        num = num // 10
        total = total + d

    return total

#Taking input
num = int(input('Enter Number: '))

#Function call
res = addition(num)

print('Sum of digits =', res)