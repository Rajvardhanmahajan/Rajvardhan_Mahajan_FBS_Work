#12. Write a program to check if given 3 digit number is a palindrome or not.

Num = int(input('Enter the number: '))

temp = Num

d1 = temp % 10
temp = temp // 10

d2 = temp % 10
temp = temp // 10

d3 = temp % 10
temp = temp // 10

rev = (d1 * 100) + (d2 * 10)  +  (d3)

#condition
if Num == rev :
    print('The number is palindrom.')
else:
    print('The number is not palindrom.')