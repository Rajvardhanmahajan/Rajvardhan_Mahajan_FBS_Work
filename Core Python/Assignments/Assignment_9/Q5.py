#5. Write a program to find factorial using recursion.

def factorial(num, fact):       #Function Defination
    if num == 1:
        return 1
    
    #Perform operation
    return num * factorial(num-1, fact)


#Take input
num = int(input('Enter Number: '))
fact = 1

#Function call
res = factorial(num, fact)

print(f'Factorial of num is {res}.')

