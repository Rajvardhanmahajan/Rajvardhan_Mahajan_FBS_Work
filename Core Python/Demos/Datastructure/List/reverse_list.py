li = [60, 50, 40, 30, 20, 10]

beg = 0

end = len(li) - 1

while beg < end:

    li[beg], li[end] = li[end], li[beg]
    beg += 1
    end -= 1

print(li)