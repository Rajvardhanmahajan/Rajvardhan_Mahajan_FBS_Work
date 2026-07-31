#1. Python Program to Replace all Occurrences of ‘a’ with $ in a String.

#Function to replace characters
def replace_character(text):
    result = ''

    #Traversing the string
    for ch in text:

        #Replace 'a' with '$'
        if ch == 'a':
            result += '$'
        else:
            result += ch

    # Display the result
    print("Original String :", text)
    print("Modified String :", result)   


#Main program
text = 'banana'

#Call the Function
replace_character(text)


