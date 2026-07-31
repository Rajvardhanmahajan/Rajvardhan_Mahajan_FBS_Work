#7. Write a program to find sum of digits using recursion.

def sod(num, sum):      #Function Defination
    if num == 0:
        return 0
    
    #perform operation

    return sod(num // 10, sum) + ( num % 10 )

num = int(input('Enter Number: '))
sum = 0

res = sod(num, sum)

print(res)