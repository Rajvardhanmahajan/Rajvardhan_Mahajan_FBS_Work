#To check given number is armostrong number or not.

num = int(input('Enter the Number: '))

temp = num

count = 0

while num > 0:      #This while loop is use to count digits in num.
    count += 1
    num = num // 10
# print(f'count = {count} and number is {num}')

num = temp

Total = 0

while num > 0:      #This is for digits separate out and operation.
    d = num % 10
    Total = Total + (d ** count)
    num = num // 10

if temp == Total:
    print(f'The number is armstrong.')
else:
    print(f'The number is not an armstrong.')
