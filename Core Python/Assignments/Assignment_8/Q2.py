#2. Write a program to calculate area of circle.

def area(radius):    #Function Defination

    #Perform operation
    a = 3.14 * radius ** 2

    return a

#Taking input
r = int(input('Enter radius of Circle: '))

#Function call
res = area(r)

#Display result
print(f'Area of Circle is {res}.')
