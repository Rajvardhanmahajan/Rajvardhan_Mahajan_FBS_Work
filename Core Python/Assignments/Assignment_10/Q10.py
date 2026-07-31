#10. Write a program to remove all occurrences of a given element in the list.

def remove_all_occure(li, element, new_list):
    
    for num in li:
        if num != element:
            new_list.append(num)

    print("Original List:", li)
    print("Updated List:", new_list)


li = [10, 20, 30, 40, 10, 50, 10, 60]

element = 10

new_list = []

remove_all_occure(li, element, new_list)
