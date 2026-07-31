#4. Write a program to find sum of n numbers using recursion.

def addition(n):        #Function Defination
    if n == 0:
        return 0
    
    return n + addition(n - 1)

#Taking inputs
n = int(input('Enter Number: '))
sum = 0

#Function call
res = addition(n)

#Display result
print(f'The sum of n numbers is {res}.')