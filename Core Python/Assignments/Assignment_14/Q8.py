# 8. Write a Python program to find all the anagrams and group them
# together from a given list of strings.


# Function to group anagrams
def group_anagrams(words):

    anagram_dict = {}

    # Traverse every word
    for word in words:

        # Sort the word
        key = ''.join(sorted(word))

        # Check whether the key already exists
        if key in anagram_dict:
            anagram_dict[key].append(word)
        else:
            anagram_dict[key] = [word]

    # Display grouped anagrams
    print("Grouped Anagrams:")

    for group in anagram_dict.values():
        print(group)


# Main Program

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

group_anagrams(words)