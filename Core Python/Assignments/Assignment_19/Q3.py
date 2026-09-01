# 3. Count the number of spaces in a string (take input from user)

s = input("Enter string: ")

count = sum(1 for ch in s if ch == ' ')

print("Spaces =", count)