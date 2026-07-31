def creatList(li):
    n = int(input('How many elements you want add: '))
    for i in range(n):
        ele = int(input('Enter element: '))
        li.append(ele)

    
li = []

creatList(li)

print(li)
