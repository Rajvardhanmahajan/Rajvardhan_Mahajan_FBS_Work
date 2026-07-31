#6. Write a program to print Fibonacci series using recursion.

def fibonacci(num):     #Function defination
    if num == 1 or num == 2:
        return 1
    
    #Perform operation
    return fibonacci(num - 1) + fibonacci(num - 2)

#Take input
num = int(input('Enter Number: '))

#Take for iterate value
for i in range(1 , num + 1):
    print(fibonacci(i), end=' ')