#7. Python Program to Calculate the Length of a String Without Using a Library Function

# Function to calculate string length
def string_length(text):

    count = 0

    # Traverse the string
    for ch in text:
        count += 1

    # Display the length
    print("String :", text)
    print("Length :", count)


# Main Program

text = "Rajvardhan"

# Call the function
string_length(text)