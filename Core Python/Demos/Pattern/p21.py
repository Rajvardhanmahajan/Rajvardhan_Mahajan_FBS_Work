k = 1
for i in range(1, 6):
    for j in range(i , 6):
        print(j, end=' ')

    for j in range(1, k):
        print(' ', end=' ')
    k += 2

    for j in range(5, i - 1, -1):
        print(j, end=' ')
    print()

k = 7
#left side
for i in range(4, 0, -1):
    for j in range(i, 6):
        print(j, end=' ')
    
    #Middle space
    for j in range(1, k):
        print(' ', end=' ')
    k -= 2

    #Right side
    for j in range(5, i - 1, -1):
        print(j, end=' ')

    print()
    