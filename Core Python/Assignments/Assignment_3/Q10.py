#10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

#Take input
gender = input('Enter gender Male/Female: ')

age = int(input('Enter age: '))

#Perform operation
if (gender == 'Female'):
    if (age > 18):
        print('Girl is eligible for Marriage.')
    else:
        print('Girl is not eligible for Marriage.')
else:
    if (age > 21):
        print('Boy is eligible for Marriage.')
    else:
        print('Boy is not eligible for marriage.')