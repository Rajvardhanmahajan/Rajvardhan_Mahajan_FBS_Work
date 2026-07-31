#5. Python Program to Count the Number of Vowels in a String

def count_vowels(text):

    count = 0

    # Traverse the string
    for ch in text:

        # Check whether the character is a vowel
        if ch in "aeiouAEIOU":
            count += 1

    # Display the result
    print("String          :", text)
    print("Number of Vowels:", count)


# Main Program

text = "Rajvardhan aeiou"

count_vowels(text)