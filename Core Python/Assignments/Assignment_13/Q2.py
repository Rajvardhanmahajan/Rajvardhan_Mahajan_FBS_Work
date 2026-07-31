#2. Python Program to Concatenate Two Dictionaries Into One

# Function to concatenate two dictionaries
def concatenate_dictionary(dict1, dict2):

    merged_dict = {}

    # Copy key-value pairs from the first dictionary
    for key in dict1:
        merged_dict[key] = dict1[key]

    # Copy key-value pairs from the second dictionary
    for key in dict2:
        merged_dict[key] = dict2[key]

    # Display the merged dictionary
    print("Concatenated Dictionary:")

    for key in merged_dict:
        print(key, ":", merged_dict[key])


# Main Program

dict1 = {
    "Id": 101,
    "Name": "Rajvardhan"
}

dict2 = {
    "Address": "Pune",
    "Salary": 50000
}

# Call the function
concatenate_dictionary(dict1, dict2)