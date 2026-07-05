#11. Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

#Take input

P1 = int(input('Enter age of 1st person : '))
P2 = int(input('Enter age of 2nd person : '))
P3 = int(input('Enter age of 3rd person : '))
P4 = int(input('Enter age of 4th person : '))
P5 = int(input('Enter age of 5th person : '))

ticket = int(input('Enter ticket amount: '))
total_amount = 0 

#person 1
if P1 <= 12:
    amount1 = ( ticket - (ticket * 30 /100))
elif P1 >= 59:
    amount1 =(ticket - (ticket * 50 / 100))
else:
    amount1 = (ticket)


#person 2
if P2 <= 12:
    amount2 = (ticket - (ticket * 30 /100))
elif P2 >= 59:
    amount2 = (ticket - (ticket * 50 / 100))
else:
    amount2 = (ticket)


#person 3
if P3 <= 12:
    amount3 = (ticket - (ticket * 30 /100))
elif P3 >= 59:
    amount3 = (ticket - (ticket * 50 / 100))
else:
    amount3 = (ticket)


#person 4
if P4 <= 12:
    amount4 = (ticket - (ticket * 30 / 100))
elif P4 >= 59:
    amount4= (ticket - (ticket * 50 / 100))
else:
    amount4 = (ticket)


#person 5
if P5 <= 12:
    amount5 = ( ticket - (ticket * 30 /100))
elif P5 >= 59:
    amount5 = (ticket - (ticket * 50 / 100))
else:
    amount5 = (ticket)



total_amount = amount1 + amount2 + amount3 + amount4 + amount5
    
print(f'Total amount of five persons ticket is {total_amount}')