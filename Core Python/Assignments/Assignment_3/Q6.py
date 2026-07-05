#6. Write a program to calculate profit or loss.

#Take input
cp = int(input('Enter Cost Price: '))
sp = int(input('Enter Selling Price: '))

#Perform operation
amount = sp - cp

if (amount > 0):
    print(f'Profit= {amount}.')
elif(amount < 0):
    print(f'Loss= {amount}.')
else:
    print(f'No loss No Profit!!')