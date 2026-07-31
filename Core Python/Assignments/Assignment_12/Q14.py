#14. Python Program to count the occurrences of each word in a string.

# Function to count word occurrences
def count_word_occurrences(text):

    # Convert the string into a list of words
    words = text.split()

    # Create an empty dictionary
    word_count = {}

    # Count each word
    for word in words:

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Display the result
    print("Word Occurrences:")

    for word, count in word_count.items():
        print(word, ":", count)


# Main Program

text = "cat dog cat lion dog cat"

count_word_occurrences(text)