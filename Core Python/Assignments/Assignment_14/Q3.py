#3. Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.

# Program to find unique words and their frequency using a set

# Function to count the frequency of words
def count_word_frequency(word_list):

    # Create a set of unique words
    unique_words = set(word_list)

    print("Unique Words :", unique_words)
    print("\nWord Frequency:")

    # Traverse the unique words
    for word in unique_words:

        count = 0

        # Count occurrences in the original list
        for item in word_list:
            if word == item:
                count += 1

        print(word, ":", count)
    
# Main Program

word_list = ["cat", "dog", "cat", "lion", "dog", "cat"]

# Call the function
count_word_frequency(word_list)