#3. Write a program to reverse a given number using recursive function.

#Function Defination
def reverse(num, rev):

    if num == 0:
        return rev

    d = num % 10

    return reverse(num // 10, rev * 10 + d)

#Taking input 
num = int(input("Enter Number: "))
rev = 0

#Function call
res = reverse(num, rev)

#Display result
print("Reverse =", res)