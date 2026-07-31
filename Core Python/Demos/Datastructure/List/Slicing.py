li = [10, 20, 30, 40, 50, 60, 70]

res = li[0:3]
# res = li[0:5:2]
# res = li[5:0:-2]
# res = li[:4]
# res = li[3:]
# res = li[:]
# res = li[:7]
# res = li[::]
# res = li[::-1]
# res = li[::2]

# print(res)

# sum = 0
# for i in res: 
#     sum += i
# print(sum)

sum = 0
for i in range(0, len(li), 2):   #10, 30, 50, 70
    sum += li[i]

print(sum)