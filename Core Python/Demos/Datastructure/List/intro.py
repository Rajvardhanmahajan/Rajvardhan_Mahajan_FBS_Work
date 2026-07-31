# #1 Structure: Denoted by []
# li = [10, 3.14, 'ABC']


# #2Type of data: Heterogeneous


# #3 Sequence: Ordered

# #4 Changeble:
# print(id(li))
# li[0] = 30
# print(id(li))
# print(li)


# #5. Duplication: Allowed

# li = [10, 20, 30, 10, 20]

# print(li)


li = [10, 20, 30, 10, 20]
sum = 0

print(li[-1])
print(li[0])

#method 1: loop
# for val in li:
#     sum += val
# print(sum)


#method 2: Indexing 
for i in range(len(li)):
    sum += li[i]

print(sum)