#9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String.

# Function to count words and characters
def count_words_characters(text):

    character_count = 0
    word_count = 1

    # Traverse the string
    for ch in text:

        # Count every character
        character_count += 1

        # Count words by counting spaces
        if ch == ' ':
            word_count += 1

    # Display the result
    print("String            :", text)
    print("Number of Words   :", word_count)
    print("Number of Characters :", character_count)


# Main Program

text = "I am good in Python"

count_words_characters(text)