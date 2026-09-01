# 5. Write a Python program to find the longest common prefix of all
# strings. Use the Python set.

# Program to find the longest common prefix using a set

# Function to find the longest common prefix
def longest_common_prefix(words):

    prefix = ""

    # Find the length of the shortest string
    min_length = len(words[0])

    for word in words:
        if len(word) < min_length:
            min_length = len(word)

    # Compare characters index by index
    for i in range(min_length):

        char_set = set()

        # Add characters at the same index into the set
        for word in words:
            char_set.add(word[i])

        # If all characters are the same
        if len(char_set) == 1:
            prefix += words[0][i]
        else:
            break

    print("Longest Common Prefix :", prefix)


# Main Program

words = ["flower", "flow", "flight"]

longest_common_prefix(words)