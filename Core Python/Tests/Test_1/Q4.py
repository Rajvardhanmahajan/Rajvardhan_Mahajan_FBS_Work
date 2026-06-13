

#Take input
Area_1wall = int(input('Enter area of wall: '))
interior_cost = int(input('Enter Cost of interior wall as market: '))
exterior_cost = int(input('Enter Cost of exterior wall as market price: '))

#operation

walls = Area_1wall * ( 7 * 2 )

int_cost = interior_cost * walls
ext_cost = exterior_cost * walls


#display

print(f'The cost of Interior walls is {int_cost} and the cost of Exterior walls is {ext_cost}.')


