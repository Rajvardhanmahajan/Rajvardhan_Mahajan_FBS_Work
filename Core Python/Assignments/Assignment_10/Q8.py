#8. Write a program to create a duplicate of an existing list. It should not point to same list.

def dupliList(li):
    for i in li:
        temp.append(i)

    print(id(li))
    print('Original string: ', li)
    print(id(temp))
    print('Duplicate list: ', temp)

li = [10, 20, 30, 40, 50, 60]

temp = []

dupliList(li)