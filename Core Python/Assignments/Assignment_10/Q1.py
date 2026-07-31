#1. Write a program to find sum of all elements of list
def creatList(li):
    n = int(input('Enter how many elements you want to put: '))
    for i in range(n):
        ele = int(input('Enter element: '))
        li.append(ele)


def add(li, sum):

    for i in li:
        sum += i

    return sum


li = []

creatList(li)

print('List: ',li)

res = add(li, 0)

print('Addition :',res)