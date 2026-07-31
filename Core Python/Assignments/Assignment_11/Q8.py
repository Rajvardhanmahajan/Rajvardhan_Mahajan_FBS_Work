#8. Print 1 to 100 in snakes and ladder pattern.

# Function to print the pattern
def print_snakes_ladder():

    start = 1

    # Print 10 rows
    for row in range(10):

        # Even row: Left to Right
        if row % 2 == 0:
            for num in range(start, start + 10):
                print(f"{num:3}", end=" ")

        # Odd row: Right to Left
        else:
            for num in range(start + 9, start - 1, -1):
                print(f"{num:3}", end=" ")

        print()

        # Move to the next row
        start += 10


# Main Program
print_snakes_ladder()

