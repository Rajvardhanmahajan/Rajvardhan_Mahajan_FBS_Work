#Merger sort 

#Conquer/ merge the divided list
def conquer(li, start, mid, end):
    temp = []                           #Create a empty list
    left = start                        
    right = mid + 1                     

    # Compare elements from both halves
    while left <= mid and right <= end:
        if li[left] < li[right]:
            temp.append(li[left])
            left += 1
        else:
            temp.append(li[right])
            right += 1
    
    # Copy remaining elements from left half
    while left <= mid:
        temp.append(li[left])
        left += 1
    
    # Copy remaining elements from right half
    while right <= end:
        temp.append(li[right])
        right += 1

    k = start

    for x in temp:
        li[k] = x
        k += 1

#divide the each element separete
def divide(li, start, end):
    if start < end:
        mid = (start + end) // 2
        divide(li, start, mid)
        divide(li, mid+1, end)

        conquer(li, start, mid, end)

li = [7, 1, 18, 33, 69, 12]
print(f'List before sorting: {li}')

divide(li, 0, len(li)-1)
print(f'List after sorting: {li}')
