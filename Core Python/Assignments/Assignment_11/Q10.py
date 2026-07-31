#10. Write a program to print list after removing even numbers.

#Function to remove even numbers
def remove_evennumbers(numbers, new_list):

        #range 
        for num in numbers:
                if num % 2 != 0:
                        new_list.append(num)

        print('Original List                  :', numbers)
        print('List after remove even numbers :', new_list)


#Main program
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

new_list =[]

remove_evennumbers(numbers, new_list)