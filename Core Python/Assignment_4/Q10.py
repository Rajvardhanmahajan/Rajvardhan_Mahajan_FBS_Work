#10. WAP to check if given number is Perfect Number.

num = int(input('Enter the Number: '))

sum = 0 


for i in range(1, num):
    if num % i == 0:
        sum = sum + i 


if sum == num :
    print('Perfect Number: ')
else:
    print('Not Perfect Number: ')



#Universal program to find factors.
# num = int(input('Enter Number: '))

# for i in range(1, num+1):
#     if num % i == 0:
#         print(i)