# (e) x - x²/3 + x³/5 - x⁴/7 + ... n terms

x = int(input('Enter x: '))
n = int(input('Enter number of terms: '))

den = 1
total = 0

for i in range(1, n+1):

    if i % 2 == 1:
        total = total + (x ** i) / den
    else:
        total = total - (x ** i) / den

    den += 2

print(f'{total:.2f}')
    