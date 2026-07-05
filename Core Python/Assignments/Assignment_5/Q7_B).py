# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

#Take input
n = int(input('Enter value of n: '))

#perform operation
total = 0

for i in range(1, n + 1):

    total = total + (n ** i)        #increment exponent by +1. Hence, we use i

print('Total', total)