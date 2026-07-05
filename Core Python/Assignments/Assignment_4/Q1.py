#1. WAP to print all even numbers until n.

#Take input
n = int(input('Enter value of n: '))

count = 0
#Perform operation
for i in range(2, n+1, 2):

    count = count + 1

    print(i)

print('Total even Numbers:', count)


# #Second way

# # n = int(input('Enter value of n: '))

# # for i in range(2, n + 1):
    
#     # if i % 2 == 0:
#         # print(i)

















