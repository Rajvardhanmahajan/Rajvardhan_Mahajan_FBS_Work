# Program to count the frequency of words using a dictionary

# Function to count the frequency of words
def count_word_frequency(text):

    # Convert the string into a list of words
    words = text.split()

    # Create an empty dictionary
    frequency = {}

    # Count the frequency of each word
    for word in words:

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    # Display the result
    print("\nWord Frequencies:")

    for key, value in frequency.items():
        print(key, ":", value)


# Main Program

text = "cat dog cat lion dog cat"

# Call the function
count_word_frequency(text)