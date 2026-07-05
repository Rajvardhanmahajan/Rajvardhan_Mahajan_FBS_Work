#6. WAP to check if a given number is prime or not.
no = int(input('Enter value of n: '))

if no <= 1:
    pass
else:

    for i in range(2, no):
        if no % i == 0:
            print(f'{no} is not prime Number.')
            break
    else:
        print(f'{no} is a prime Number.')



#To print prime numbers between given range.

# start = int(input('Enter the Start Value: '))
# end = int(input('Enter the End Value: '))

# for no in range(start , end+1):     # 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#     if no > 1:
#         for i in range(2, no):      #here i between 2 to no value. 
#             if no % i == 0:
#                 break
#         else:
#             print(no)


