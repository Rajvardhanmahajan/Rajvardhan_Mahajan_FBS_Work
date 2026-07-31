#1^1 + 2^2 + 3^3+ ...... n^n


def addition(num):      #Function Defination
    total = 0
    i = 1

    #Perform operation
    # for i in range(1, num+1):
    while i <= num:
        total = total + ( i ** i)
        i += 1

    return total

#Taking input
n = int(input('Enter Number: '))

#Function call
res = addition(n)

#Display result
print(f'Addition is {res}.')
