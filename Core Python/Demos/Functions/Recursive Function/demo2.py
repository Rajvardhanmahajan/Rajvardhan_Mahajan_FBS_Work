#Write a program to calculate factorial using recursive function.

def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num - 1)
    

num = int(input('Enter value of: '))
res = fact(num)
print(res)
