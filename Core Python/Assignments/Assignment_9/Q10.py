#10. Write a program to reverse a number using recursion.

#Function defination
def reverse(num, rev):
    if num == 0:
        return rev
    
    #Perform operation
    d = num % 10

    return reverse(num // 10, rev * 10 + d)

#Taking input
num = int(input('Enter Number: '))

#Function call
res = reverse(num, 0)

#Display result
print(res)