#8. Python Program to Remove the Characters of Odd Index Values in a String.

def remove_odd_index_characters(text):

    result = ""

    for i in range(len(text)):

        # Skip odd index characters
        if i % 2 != 0:
            continue

        # Add only even index characters
        result += text[i]

    print("Original String :", text)
    print("Modified String :", result)


text = "Rajvardhan"

remove_odd_index_characters(text)