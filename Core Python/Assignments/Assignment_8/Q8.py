#8. Write a program find reverse of a number.

def reverse(num):       #Function Defination
    temp = num
    rev = 0

    #Perform operation
    while temp > 0:
        d = temp % 10
        temp = temp // 10

        rev = rev * 10 + d

    return rev

#Taking Input
num = int(input('Enter Number: '))

#Function call
res = reverse(num)

print(f'Reverse Number is {res}.')