#Digit separate out using while loop.

num = int(input('Enter Number: '))

temp = num

while (temp > 0):
    d = temp % 10
    temp = temp // 10
    print(d)
    print(temp)