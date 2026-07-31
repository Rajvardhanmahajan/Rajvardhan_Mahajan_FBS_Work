# Take element from user and and fine linear sarch.

#Create list Using user input

def createli(li):       #Function defination
    n = int(input('Enter how many number you want to put: '))
    for i in range(n):
        ele = int(input('Enter and Number: '))
        li.append(ele)

#Search an element using linear search algorithms

def linearsear(li,searEle):     #Function defination
    for i in range(len(li)):
        if li[i] == searEle:
            return i
    
    return -1


li = []     #list

createli(li)    #Function call 

print('List:', li)

searEle = int(input('Enter element to search: '))

res = linearsear(li, searEle)

if res != -1:
    print(f'{searEle} found at index {res}.')
else:
    print(f'{searEle} not found in the list')
