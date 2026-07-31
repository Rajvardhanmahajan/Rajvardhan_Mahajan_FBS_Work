#To find the sum of element of list.

li = [[10, 20],[30, 40],[50, 60]]

# size = len(li)
sum = 0

for i in range (len(li)):
    for j in range(len(li[i])):
        sum = sum + li[i][j]

print(sum)



#Print sum value of list
li = [10, 20, 30, 40, 50, 60]

sum = 0
# for val in li:
#     sum += val
# print(sum)

for i in range(len(li)):
    sum += li[i]

print(sum)