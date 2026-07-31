#1. Write a program to calculate area of rectangle.

def area(length, breadth):  #Function Defination

    #Perform operation
    return length * breadth

#Taking input
x = int(input('Enter Length of rectangle: '))
y = int(input('Enter Breadth of rectangle: '))

#function call
res = area(x, y)

#Display result
print(f'Area of rectangle is {res}.')


