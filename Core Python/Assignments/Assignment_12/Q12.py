#12. Python Program to count number of lowercase characters in a string.

# Function to count lowercase letters
def count_lowercase(text):

    lowercase_count = 0

    # Traverse the string
    for ch in text:

        # Check whether the character is lowercase
        if 'a' <= ch <= 'z':
            lowercase_count += 1

    # Display the result
    print("String                      :", text)
    print("Number of Lowercase Letters :", lowercase_count)


# Main Program

text = "Rajvardhan"

# Call the function
count_lowercase(text)