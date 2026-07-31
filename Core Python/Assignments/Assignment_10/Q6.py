#6. Write a program to remove duplicates from the list.

def removeDupli(li):
    
    for i in li:
        if i not in temp:
            temp.append(i)

    print('Original List:', li)
    print('After Removing Duplicates:', temp)


li = [10, 20, 30, 40, 50, 30, 40, 60, 20, 70]

temp = []

removeDupli(li)

