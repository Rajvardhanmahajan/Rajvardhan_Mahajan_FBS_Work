# 5. Sum of all prime numbers between 1 to n.

# def isprime(num):       #Function defination
    
#     total = 0
#     i = 2

#     #Taking value upto n
#     while i <= num:

#         j = 2
#         prime = True

#         #Use value of j to check prime or not
#         while j < i:
#             if i % j == 0:
#                 prime = False
#                 break
#             j += 1

#         #Total of prime num
#         if prime:
#             total = total + i

#         i += 1

#     return total

# #Taking input
# num = int(input('Enter Number: '))

# #Function call
# res = isprime(num)

# print('Sum of Prime Numbers =', res)
