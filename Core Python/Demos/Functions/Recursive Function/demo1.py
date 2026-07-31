 #sum of series

def series(n):
    if n == 0:
        return 0
    else:
        return n + series(n-1)

n = int(input('Enter value of n: '))

res = series(n)
print(res)

