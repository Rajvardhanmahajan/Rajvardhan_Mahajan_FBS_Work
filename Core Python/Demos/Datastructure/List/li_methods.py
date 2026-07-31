li = [30, 10, 40, 20, 40, 40]

# li.append(50)           #Add values to the end of list.
# li.append((60, 70))          #Only on value can add using append. This is add in tuple format.

# li.clear()          #It is use to clear list

# li2 = li.copy()       #Copy the li and assign to li2.

# li3 = li                #Address li is assign to li2.

# li.append(50)       # Only the change in li3 becouse of same address.
# print(li2)
# print(li3)


# print(li.count(40))     #Print how many times the given numbers is present in list.

# li.extend([60, 70, 80])   #Multiple values can be add to end of list.

# print(li.index(20))         #Writing index value of 20

li.insert(2, 50)
li.pop(2)
li.sort()
# li.sort(reverse= True)
print(li)