#b. 1!+ 2! + 3! + 4!+..... + n!


def addition(factorial):        #Function defination
    fact = 1
    total = 0
    i = 1
    
    #perfrom operation
    while i <= factorial:
    # for i in range(1, factorial+1):
        fact = fact * i
        i = i + 1
     
        total = total + fact

    return total

#Taking input
n = int(input('Enter Number: '))

#Function call
res = addition(n)

#display result
print(f'Factorial of n Numbers is {res}.')

