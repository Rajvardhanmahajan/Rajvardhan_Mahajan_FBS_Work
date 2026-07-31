#Given string is palindrom or not / reverse

# str = 'Firstbeat'

# rev = ''

# for ch in range(len(str)-1, -1, -1):
#     rev += str[ch]

# print('Reversed string:',rev)


# 2)
# str = 'Firstbeat'

# rev = ''

# for ch in str:
#     rev = ch + rev

# print('Reversed String:', rev)


#3)Using Two pointers 


# s = input('Enter a string: ')

# li = list(s)

# left = 0
# right = len(li)-1

# while left < right:
#     li[left],li[right] = li[right],li[left]
#     left += 1
#     right -= 1

# rev = ''

# for ch in li:
#     rev += ch


# print('Reversed String:', rev)


a = 2
b = 3
c = '4'

print(a + b + c)