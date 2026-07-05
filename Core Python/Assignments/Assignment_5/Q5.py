# 5. Write a program to print prime numbers between 1 to 100.

count = 0
for num in range(2, 100 + 1):

    if num <= 1:
        pass 

    for i in range(2, num):
        if num % i == 0:
            break

    else:
        count += 1
        print(num)
print(f'Total prime number between 2 to 100 is {count}.')
        