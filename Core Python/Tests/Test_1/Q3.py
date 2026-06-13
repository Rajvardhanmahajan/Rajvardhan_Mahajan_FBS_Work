#3. Write a program to accept distance in km and convert it into meters and centimeters both.

#Take input
Km = int(input('Enter Distance in Km: '))

#operation
meter = Km * 1000

centimeter = Km * 100000

#display result
print(f'Distance in meter is {meter}. And the Distance in centimeter is {centimeter}.')
