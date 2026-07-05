# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

# Take input

students = int(input("Enter Number of Students: "))

add_percentage = 0

# For each student
for i in range(1, students + 1):

    print(f"\nStudent {i}")

    total = 0

    # Take 5 subject marks
    for j in range(1, 6):

        marks = int(input(f"Enter Marks of Subject {j}: "))

        total = total + marks

    # Calculate percentage
    percentage = total / 5

    print("Percentage =", percentage)

    add_percentage = add_percentage + percentage

# Calculate average percentage
avg = add_percentage / students

print("\nAverage Percentage =", avg)