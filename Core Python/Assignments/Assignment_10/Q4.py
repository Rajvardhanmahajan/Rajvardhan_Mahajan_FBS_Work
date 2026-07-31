#4. Write a program to reverse the list.

def creatList(li):
    n = int(input('Enter how many elements you want to put: '))
    for i in range(n):
        Ele = int(input('Enter Number: '))
        li.append(Ele)
    
def reverseLi(li, beg , end):

    while beg < end:
        li[beg], li[end] = li[end], li[beg]
        beg += 1
        end -= 1


li = []

creatList(li)

print('List =', li)

beg = 0
end = len(li) - 1

reverseLi(li, beg, end)

print('Reverse List:', li)