# 4. Remove all of the vowels in a string (take input from user)

s = input("Enter string: ")

result = ''.join([ch for ch in s if ch.lower() not in 'aeiou'])

print(result)