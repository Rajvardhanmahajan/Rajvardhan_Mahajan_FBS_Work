# #11. WAP to check if given number Strong Number.

# num = int(input('Enter the Number: '))

# temp = num

# total = 0

# #Extract digit / separate digit
# while temp > 0:
#     d = temp % 10

#     #find factorial of digit
#     fact = 1

#     for i in range(1, d+1):
#         fact = fact * i

#     total = total + fact

#     temp = temp // 10

# #check Strong Number
# if total == num:
#     print('Strong Number')
# else:
#     print('Not Strong Number')




start = int(input('Enter Start Number: '))
end = int(input('Enter end Number: '))


for num in range(start, end+1):
    temp = num
    total = 0

    while temp > 0:
        d = temp % 10
        fact = 1

        for i in range(1, d + 1):
            fact = fact * i

        total = total + fact

        temp = temp // 10

    if total == num:
        print(num)