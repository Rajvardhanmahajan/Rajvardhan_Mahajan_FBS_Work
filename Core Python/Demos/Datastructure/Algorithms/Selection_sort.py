
def selectionSort(li):
    size = len(li)
    for i in range(0, size - 1):    #for index positions
        min_ind = i
        for j in range(i + 1, size):    #for compare elements
            if (li[min_ind] > li[j]):
                min_ind = j
        
        #Swapping elements
        li[i], li[min_ind] = li[min_ind], li[i]
        # print(li)                                       for checking the flow

li = [60, 50, 40, 30, 20, 10]
selectionSort(li)
print(f'List afte sorting: ', li) 