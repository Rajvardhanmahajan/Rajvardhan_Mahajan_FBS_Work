# 2. Write a program to check if given number is Armstrong or not using recursive
# function.

#Function Defination
def isArmstrong(num, count):
    if num == 0:
        return 0
    
    digit = num % 10
    return isArmstrong(num // 10, count) + (digit ** count)

#Take input
num = int(input('Enter value of num: '))
count = len(str(num))

#Function call
res = isArmstrong(num, count)

#Display result
if res == num:
    print(f'{num} is armstrong.')
else:
    print(f'{num} is not armstrong.')

