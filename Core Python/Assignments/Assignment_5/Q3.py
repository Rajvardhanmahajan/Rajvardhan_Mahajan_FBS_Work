# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

#Take input
passengers = int(input('Enter Number of passengers: '))

ticket = int(input('Enter ticke amount: '))

total = 0

for i in range(1 , passengers + 1):

    age = int(input(f'Enter age of person {i}: '))

    if age < 12:
        pay = ticket - (ticket * 30 / 100)

    elif age > 59:
        pay = ticket - (ticket * 50  / 100)

    else:
        pay = ticket 


    total = total + pay

print('Total ticket amount =', total)