#8. Write a program to check whether a number is prime or not using recursion.

#Function defination
def isprime(num, i):
    if num <= 1:
        return False
    
    if i == num:
        return True
    
    if num % i == 0:
        return False
    
    return isprime(num, i+1)

   
#Taking input
num = int(input('Enter Number: '))

if isprime(num, 2):
    print('Prime Number.')
else:
    print('Not Prime Number.')

