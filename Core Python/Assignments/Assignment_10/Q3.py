#3. Write a program to find the second largest element in the list.

def createList(li):
    n = int(input('Enter How many elements you want to put: '))

    for i in range(n):
        ele = int(input('Enter Numbers: '))
        li.append(ele)


def SeLargeEle(li, max, sec):
    
    for i in range(len(li)):
        if li[i] > max:
            max = li[i]

    for j in li:
        if j > sec and j != max:
            sec = j

    return sec

li = []

createList(li)

print('List =', li)

max = li[0]
sec = li[0]

res = SeLargeEle(li, max, sec)

print('Second Largest Element:', res)



