#3. Convert distant given in feet and inches into meter and centimeter.

#Take input
feet = int(input('Enter Feet: '))
inches = int(input('Enter Inches: '))

#Perform operation
Total_inches = (feet * 12 ) + inches

cm = Total_inches * 2.54 

meter = cm / 100

#Display result 
print(f'Distance in meter is {meter}.')
print(f'Distance in centimeter is {cm}.')