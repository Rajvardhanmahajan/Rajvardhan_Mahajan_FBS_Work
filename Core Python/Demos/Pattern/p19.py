k = 7

for i in range(1, 6):
    for j in range(1, i +1):
        print(chr(64 + j), end=' ')

    for j in range(1, k + 1):
        print(' ',end=' ')
    k -= 2

    for j in range(i, 0 , -1):
        if(chr(64+j) != 'E'):
            print(chr(64+j),end=' ')

    print()

k=1
for i in range(1, 5):
    for j in range(1, 6-i):
        print(chr(64+j), end=' ')


    for j in range(k):
        print(' ', end=' ')
    k += 2
    
    for j in range(5-i, 0, -1):
        # if j != i:
        print(chr(64+j), end=' ')
    print()
    