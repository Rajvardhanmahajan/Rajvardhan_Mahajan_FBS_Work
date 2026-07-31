#4. Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged.

# Function to swap the first and last characters
def swap_first_last(text):

    # Convert the string into a list
    characters = list(text)

    # Swap the first and last characters
    characters[0], characters[-1] = characters[-1], characters[0]

    # Convert the list back into a string
    result = "".join(characters)

    # Display the result
    print("Original String :", text)
    print("Modified String :", result)


# Main Program

text = "Rajvardhan"

# Call the function
swap_first_last(text)