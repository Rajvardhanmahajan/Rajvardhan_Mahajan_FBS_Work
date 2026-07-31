#11. Python Program to replace every blank space with hyphen in a string.

# Function to replace spaces with hyphens
def replace_spaces(text):

    result = ""

    # Traverse the string
    for ch in text:

        # Replace blank space with hyphen
        if ch == ' ':
            result += '-'
        else:
            result += ch

    # Display the result
    print("Original String :", text)
    print("Modified String :", result)


# Main Program

text = "I am good in coding"

# Call the function
replace_spaces(text)