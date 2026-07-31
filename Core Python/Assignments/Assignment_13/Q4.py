#4. Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

# Function to create the dictionary
def generate_dictionary(n):

    number_dict = {}

    # Generate key-value pairs
    for num in range(1, n + 1):
        number_dict[num] = num * num

    # Display the dictionary
    print("Generated Dictionary:")

    for key, value in number_dict.items():
        print(key, ":", value)


# Main Program

n = int(input("Enter the value of n: "))

# Call the function
generate_dictionary(n)
