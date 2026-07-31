
def binarySearch(li, SearchEle):

    beg = 0
    end = len(li) - 1

    while (beg <= end):
        print('while...')

        mid = (beg + end) // 2

        if (SearchEle == li[mid]):
            return mid
    
        elif (SearchEle < li[mid]):
            end = mid - 1

        elif (SearchEle > li[mid]):
            beg = mid + 1

    else: 
        return -1
    
li = [10, 20, 30, 40, 50, 60, 70]

ele= int(input('Enter searchEle: '))

res = binarySearch(li, ele)

if res != -1:
    print(f'{ele} is found at index position {res}.')
else:
    print(f'{ele} is not present in list.')