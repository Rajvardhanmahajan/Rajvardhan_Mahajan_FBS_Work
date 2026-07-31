#3. Python Program to Check if a Given Key Exists in a Dictionary or Not

# Program to check whether a key exists in a dictionary

def exists_in_dictionary(di):

    # Accept the key from the user
    search_key = input("Enter the key to search: ")

    # Check whether the key exists
    if search_key in di:
        print("Key Found.")
        print("Value :", di.get(search_key))
    else:
        print("Key Not Found.")


# Main Program

di = {
    "Id": 101,
    "Name": "Rajvardhan",
    "Language": "Python",
    "Mo_No": 8010
}

exists_in_dictionary(di)