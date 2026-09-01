# 6. Use a dictionary comprehension to count the length of each word
# in a sentence (take input from user)

s = input("Enter sentence: ")

result = {word: len(word) for word in s.split()}

print(result)