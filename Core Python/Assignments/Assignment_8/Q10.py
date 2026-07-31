#10. Write a program to check if entered year is a leap year or not.

def isleaf(year):       #Function Defination

    #Perform operation
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

#Taking input
year = int(input('Enter Year: '))

#Function call
res = isleaf(year)

if res:
    print('Leaf Year')
else:
    print('Not a Leap Year')