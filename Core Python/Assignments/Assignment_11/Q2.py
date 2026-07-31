#2. Python Program to Merge Two Lists and Sort it

# Function to merge two lists
def Merge_two_list(li1, li2, mergeli):
    
    # Add elements from the first list
    for num in li1:
        mergeli.append(num)

    # Add elements from the second list
    for num in li2:
        mergeli.append(num)



# Function to sort the merged list using Selection Sort
def selectionSort(mergeli):
    size = len(mergeli)

    # Selection Sort
    for i in range(0, size-1):
        min_ind = i
        for j in range(i+1, size):
            if mergeli[min_ind] > mergeli[j]:
                min_ind = j

        #swapping elements
        mergeli[i],mergeli[min_ind] = mergeli[min_ind],mergeli[i]


# Main Program
li1 = [10, 20, 40]
li2 = [60, 50, 30]

mergeli = []

# Merge both lists
Merge_two_list(li1, li2, mergeli)

print('Merged List:',mergeli)

selectionSort(mergeli)

print('\nList after sorting :', mergeli)