

#Take input
CP = int(input('Enter Cost price: '))
SP = int(input('Enter Selling price: '))

#operation
Profit = SP - CP

#condition
if (Profit > 0):
    print(f'Profit= {Profit}')
elif (Profit == 0):
    print('prifi')
else:
    print('Loss')