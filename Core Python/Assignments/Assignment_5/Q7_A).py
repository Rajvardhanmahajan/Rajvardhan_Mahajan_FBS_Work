#7. Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!


#Take input
n = int(input('Enter value of n: '))

total = 0

for i in range(1, n+1):

    fact = 1

    for j in range(1, i + 1):

        fact = fact * j

    total = total + fact

print('Total =', total)



#second way 

# fact = 1
# total = 0

# for i in range(1, n+1):

#     fact = fact * i

#     total = total + fact

# print('Total =', total)

