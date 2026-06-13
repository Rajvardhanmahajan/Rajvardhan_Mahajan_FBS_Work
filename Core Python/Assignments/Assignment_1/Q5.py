#5. Write a program to enter P, T, R and calculate Compound Interest.

#Take input
#Take input
P = int(input("Enter principal amount: "))
T = int(input("Enter Duration of amount / time: "))
R = int(input("Enter amount rate: "))

#perform operation
C_I = int (P * (1 + (R /100)) ** T - P )

#display result
print(f"The principal is {P} and the rate is {R} and It's time is {T} and It's calculated compound interest is {C_I}.")
