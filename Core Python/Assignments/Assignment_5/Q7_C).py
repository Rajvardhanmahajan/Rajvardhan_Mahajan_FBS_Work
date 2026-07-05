#c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

#Take input
n = int(input('Enter n: '))

#perform operation
total = 0

for i in range(n):

    total = total + (2 ** i)

print('Total', total)