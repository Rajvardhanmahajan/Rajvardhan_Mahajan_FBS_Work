#2. Python Program to Remove the nth Index Character from a Non-Empty String.

# Function to remove the character at a given index
def remove_character(text, index):

    result = ""

    # Traverse the string using index
    for i in range(len(text)):

        # Skip the given index
        if i != index:
            result += text[i]

    # Display the result
    print("Original String :", text)
    print("Modified String :", result)


# Main Program

text = "Elephant"

index = int(input('Enter index position: '))

# Call the function
remove_character(text, index)