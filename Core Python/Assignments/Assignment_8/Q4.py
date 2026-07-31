#4. Sum of all odd numbers between 1 to n

def odd(num):       #Function Defination
    total = 0
    i = 1

    # value is less than num
    while i<= num:
        # if i % 2 != 0:
        total = total + i
        i = i + 2
    return total

#Taking input
num = int(input('Enter the Number: '))

#Function call
res = odd(num)

print(f'Sum of all odd numbers between {1} to {num} is {res}.')
