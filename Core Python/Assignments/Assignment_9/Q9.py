#9. Write a program to calculate the m to the power n using recursion.

#Function Defination
def power(m, n):
    if n == 0:
        return 1
    
    #Perform operation
    return m * power(m, n - 1)


#Taking input
m = int(input('Enter the Number: '))
n = int(input('Enter Power: '))

#Function call
res = power(m, n)

print(res)