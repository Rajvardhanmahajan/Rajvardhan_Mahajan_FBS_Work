
def factorial(num):
    fact = 1

    while num > 0:
        fact = fact * num

        num -= 1
    return fact

def isStrong(num):
    temp = num
    total = 0

    while temp > 0:
        d = temp % 10
        total = total + factorial(d)
        temp = temp // 10

    return total == num

#using filter and lambda

strong_numbers = list(filter(lambda x: isStrong(x), range(1, 1001)))

print('Strong Numbers:', strong_numbers)
