#13. Python Program to count number of digits and letters in a string.

# Function to count letters and digits
def count_letters_digits(text):

    letter_count = 0
    digit_count = 0

    # Traverse the string
    for ch in text:

        # Check whether the character is a letter
        if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
            letter_count += 1

        # Check whether the character is a digit
        elif '0' <= ch <= '9':
            digit_count += 1

    # Display the result
    print("String            :", text)
    print("Letters Count     :", letter_count)
    print("Digits Count      :", digit_count)


# Main Program

text = "Raj123Python45"

# Call the function
count_letters_digits(text)