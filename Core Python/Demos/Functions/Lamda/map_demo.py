def sq(num):
    return num ** 2

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res = list(map(sq, data))
print(res)