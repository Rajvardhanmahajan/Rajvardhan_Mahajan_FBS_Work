#Write a program to degit separate.

def dsep(num):
    # if num == 0:
    #     return 0
    
    # dsep (num // 10)
    # print(num % 10)

    if (num > 0):
        d = num % 10
        print(d)
        dsep(num // 10)

num = int(input('Enter the number: '))
dsep(num)
