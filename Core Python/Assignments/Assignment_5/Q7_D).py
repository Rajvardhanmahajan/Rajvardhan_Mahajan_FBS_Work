#d. S = a + a²/2 + a³/3 + ... + a¹⁰/10

a = int(input('Enter value of a: '))

total = 0

for i in range(1, 11):
    total = total + (a ** i) / i

print(f'{total:.2f}')       #jar decimal ntr two digit made sampayla hav tya sathi. 