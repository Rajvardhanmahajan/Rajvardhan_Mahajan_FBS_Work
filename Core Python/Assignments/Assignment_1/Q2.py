# Write an algorithm to calculate area of rectangle.
#1.START
#2.TAKE INPUT
    # l = 10
    # b = 20
#3.PERFORM OPERATION
    # AREA = l * b 
#4.Display Area
    # Area of rectangle is lenght is --- abd breadth is --- =
#5.

# START&TAKE INPUT
lenght = int(input('Enter lenght here: '))
breadth = int(input('Enter breadth here: '))

# PERFORM OPERATION
Area = lenght * breadth

#DISPLAY AREA OF RECTANGLE
#Here i use a F-string. An f-string (formatted string literal) is used to insert variables directly inside a string.
print(f"Area of rectangle is {Area} where it's length is {lenght} and it's breadth is {breadth}")

