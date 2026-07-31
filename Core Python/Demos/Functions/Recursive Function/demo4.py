#Sum of digits.
def sod(num):

    if num == 0:
        return 0
    
    else:
        return sod(num // 10) + (num % 10)

num = int(input('Enter the Number: '))

res = sod(num)

print(res)