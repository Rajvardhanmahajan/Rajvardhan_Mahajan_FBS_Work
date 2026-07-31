
for i in range(1, 5):
    for j in range(1, 5):
        
        if (j == 1 or i == j):
            print(j, end=' ')
        else:
            print(' ', end=' ')
    print()
       