#To check palindrom or not

def reverse(num, rev):
    if num == 0:
        return rev
    
    return reverse(num // 10, rev * 10 + num % 10)


def ispalindrom(num):

    rev = reverse(num, 0)

    if rev == num:
        print('palindrom')
    else:
        print('not palindrom')

num = 121

res = ispalindrom(num)


# def reverse(num, rev):

#     if num == 0:
#         return rev

#     return reverse(num // 10, rev * 10 + num % 10)


# def palindrome(num):

#     rev = reverse(num, 0)

#     if num == rev:
#         print("Palindrome")
#     else:
#         print("Not Palindrome")


# num = int(input("Enter Number: "))

# palindrome(num)

