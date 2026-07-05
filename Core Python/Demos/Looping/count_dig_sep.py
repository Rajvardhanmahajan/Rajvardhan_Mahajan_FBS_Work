#Write a program to calculate total number of digit. Available in numbers.

num = int(input('Enter Number: '))

temp = num

count = 0

while (temp > 0):
    d = temp % 10
    temp = temp // 10
    count += 1

print('Totol count:', count)