#1. Write a program to find sum of following series using recursive functions:

# i. 1! + 2! + 3! + 4! +..... + n!
# Note : For fact and sum two recursive functions

#Function for factorial
def fact(n):
    if n == 1:
        return 1
    
    return n * fact(n-1)    #recursion function- fact(n-1)

#Function for sum of series
def series(n):
    if n == 1:
        return 1
    
    return fact(n) + series(n-1)    #recursion function- series(n-1)


n = int(input('Enter value of n: '))

res = series(n)

print(f'Some of factorial upto n: {res}.')

