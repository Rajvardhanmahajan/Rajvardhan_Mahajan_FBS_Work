#Write a program to convert days into years, weeks and days.

#Take input
days = int(input('Enter days: '))

#Perform operation

years = days // 365
days = days % 365               # #Reasigning - Again assigning value to the same variable.   (# days)

weeks = days // 7
days = days % 7

#Display result
print(f'YEARS: {years}, WEEKS: {weeks}, DAYS: {days}')


                                  
                                