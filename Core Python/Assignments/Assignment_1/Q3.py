# Program to find quotient and remainder of two numbers.
#START
#TAKE INPUT
    # Dividend =50
    # Divisor = 5
#PERFORM OPERATION
#1.FIND QUOTIENT OF 
# QUOTIENT = DIVIDEND // DIVISOR
#2.FIND REMAINDER OF 
# REMAINDER = DIVIDEND % DIVISOR
#3.Display result
#4. STOP

Dividend = int(input('Enter the Dividend: '))
Divisor = int(input('Enter the Divisor: '))

#Find Quotient 
Quotient = Dividend // Divisor

#Find Remainder
Remainder = Dividend / Divisor

print(f"The Dividend is {Dividend} and the Divisor is {Divisor} and it's Quotient is {Quotient} and the it's Remainder is {Remainder}")
