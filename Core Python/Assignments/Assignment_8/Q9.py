#To check given number is palindrom or not using function.

def palindrom(num):     #Taking input

    temp = num
    rev = 0

    #Perform operation
    while temp > 0:
        d = temp % 10
        temp = temp // 10

        rev = rev * 10 + d

    return rev
    # if rev == num:
    #     return True
    # else:
    #     return False

#Taking input  
num = int(input('Enter Number: '))

#Function call
res = palindrom(num)

if res == num:
    print(f'The number is palindrom {res}.')
else:
    print(f'The number is not palindrom {res}.')

# print(res)