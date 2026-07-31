#5. Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.

def searchEle(li, Ele):
    count = 0

    for i in range(len(li)):
        if Ele == li[i]:
            count += 1
    
    if count > 0:
        print('Number is Present.')
        print('Number of times present:', count)
    
    else:
        print('Element is Not Present.')


li = [10, 30, 20, 30, 40, 50, 60, 50, 60, 50, 50, 70]

Ele = int(input('Enter search Element: '))

searchEle(li, Ele)
