#4. WAP to calculate area of triangle and rectangle

# Take input of triangle 
breadth = int(input('Enter triangle breadth: '))
height = int(input('Enter triangle height: '))

#Perform operation
area = 1 / 2 * breadth * height

#Take input of rectangle
len = int(input('Enter len of rectangle: '))
bre = int(input('Enter breadth of rectangle: '))

#perform operation 
arearectangle = len * bre

#Display result
print(f'Area of triangle is {area}.')
print(f'Area of rectangle is {arearectangle}.')