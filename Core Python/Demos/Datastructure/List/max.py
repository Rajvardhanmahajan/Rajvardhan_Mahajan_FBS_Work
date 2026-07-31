li = [34, 57, 83, 42, 23, 53, 65]

max = li[0]
min = li[0]
for i in range(len(li)):
    if (li[i] > max):
        max = li[i]

    if (li[i] < min):
        min = li[i]

print('Maximum Number:', max)
print('Minimum Number:', min)


