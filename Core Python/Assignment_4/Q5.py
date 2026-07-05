#5. WAP to print Fibonacci series upto n.

num = int(input('Enter the value of num: '))

a = -1
b = 1

for i in range (num):
    c = a + b
    print(c)
    a = b
    b = c
    




