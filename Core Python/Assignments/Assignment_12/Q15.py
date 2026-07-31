#15. Python Program to find larger string without using built-in functions.

# Function to display the larger string
def larger_string(text1, text2):

    count1 = 0
    count2 = 0

    # Count the length of the first string
    for ch in text1:
        count1 += 1

    # Count the length of the second string
    for ch in text2:
        count2 += 1

    # Compare the lengths
    if count1 > count2:
        print("Larger String :", text1)
    elif count2 > count1:
        print("Larger String :", text2)
    else:
        print("Both strings have the same length.")


# Main Program

text1 = "Rajvardhan"
text2 = "Mahajan"

larger_string(text1, text2)