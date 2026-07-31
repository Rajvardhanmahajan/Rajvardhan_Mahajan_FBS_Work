#7. Write a program to create a new list from existing list which contains cube of
# each number of list.

def cubicList(li):
    
    for i in li:
        temp.append(i ** 3)

    
    print("Original List:", li)
    print("Cube List:", temp)


li = [1, 2, 3, 4, 5, 6, 7, 8]

temp = []

cubicList(li)

