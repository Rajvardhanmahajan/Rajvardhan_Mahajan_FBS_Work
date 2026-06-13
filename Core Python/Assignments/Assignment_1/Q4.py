#4. Write a program to enter P, T, R and calculate simple Interest.

#Take input
P = int(input("Enter principal amount: "))
T = int(input("Enter Duration of amount / time: "))
R = int(input("Enter amount rate: "))

#perform operation
S_I = (P * R * T) / 100

#display result
print(f"The principal is {P} and the rate is {R} and It's time is {T} and It's calculated simple interest is {S_I}.")
