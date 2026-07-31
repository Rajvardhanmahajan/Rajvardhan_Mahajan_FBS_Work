#2. Write a program to find maximum and minimum element in a list.

def creatlist(li):
    n = int(input('Enter how many elements you want to put: '))
    for i in range(n):
        ele = int(input('Enter Number: '))
        li.append(ele)

def minmax(li,min,max):
    
    for i in range(len(li)):
        if (li[i] > max):
            max = li[i]
       
        if (li[i] < min):
            min = li[i]

    return max, min

li = []

creatlist(li)
print(f'List: {li}')

max = li[0]
min = li[0]

max, min = minmax(li,min,max)

print('Minimum =',min)
print('Maximum =',max)