#Write a program to calculate simple interest based on Principal, Rate and Time (SI = P*R*T / 100)

#Take input
Principal = int(input('Enter Principal Amount: '))
Rate = int(input('Enter Rate: '))
Time = int(input('Enter Time|Year: '))

#Operations

S_I = (Principal * Rate * Time) / 100

#Display result
print(f'The principal amount is {Principal} and Rate is {Rate} and the Time is {Time} and after calculating the Simple interest is = {S_I}.')