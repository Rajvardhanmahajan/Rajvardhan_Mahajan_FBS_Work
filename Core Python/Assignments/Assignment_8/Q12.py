#to check strong num 145 = 1!+4!+5!

def factorial(num):     #Function for factorial
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

def isstrong(num):      #Function for isstrong

    temp = num
    sum = 0

#Operation
    while temp > 0:

        d = temp % 10
        print('Digit =', d)
        temp = temp // 10

        fact = factorial(d)
        print('Factorial =', fact)

        sum = sum + fact
        print('Sum =', sum)

    if sum == num:
        return True
    else:
        return False
    
#Taking input
num = int(input('Enter value of Number: '))

#Function call
res = isstrong(num)
print(res)
