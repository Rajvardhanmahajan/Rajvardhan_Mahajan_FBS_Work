#5. WAP to calculate selling price of book based on cost price and discount.

#Take input
cost_p = int(input('Enter cost price: '))
discout = int(input('Enter discount: '))

#Perform operationn
discount_amount = (cost_p * discout) / 100

selling_p = cost_p - discount_amount

#Display
print(f'Selling price of book is {int(selling_p)}.')