def reverse(num, rev):
    if num == 0:
        return rev
    
    return reverse(num // 10, rev * 10 + num % 10)

def ispalindrom(num):
    rev = reverse(num, 0)

    if rev == num:
        print('Palindrom')
    else:
        print('Not Palindrom')

num = 145

res = ispalindrom(num)