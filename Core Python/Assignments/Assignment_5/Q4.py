# 4. WAP to print Armstrong number within a given range.

start = int(input('Enter start Number: '))
end = int(input('Enter end Number: '))

for num in range(start, end+1):

    temp = num
    count = 0

    while temp > 0:
        temp = temp // 10
        count = count + 1

    temp = num
    total = 0

    while temp > 0:
        d = temp % 10
        total = total + (d ** count)
        temp = temp // 10


    #check armstrong 
    if total == num:

        print(num)     
