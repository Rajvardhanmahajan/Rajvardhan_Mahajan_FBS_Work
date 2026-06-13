###Numeric Category
#1.int
x=10

#2. float
x =3.14

#3. complex
x = 5+ 10j

###Text Category
#1. String
x = 'Firstbeat solutions'
x = "Firstbeat solutions"

x = '''' This is first line.
This is a second line.'''

x = """"This is first line.
This is a second line."""

###Sequential Category
#1.list
x = [10, 20, 30, 40]

#2.tuple
x = (10, 20, 30, 40)

#3. range 
# x = range(1, 10)
# for i in x:
# print(i)
r = range(1, 6)

for i in r:
    print(i)


### Set type
#1.set
x = {10, 20, 30, 40}

#2.frozenset
x = frozenset({10, 20, 30, 40})


###Mapping
#1. dict
x = {1:'python', 2:'java', 3:'c'}


### Other
#1. Boolean
x = False
x = True

#2. Nonetype
x = None


# num1 = input("Enter the first number:")
# num2 = input("Enter the second number:")

# num1 = int(num1)
# num2 = int(num2)

# sum = num1 + num2
# print("The sum of",num1, "and", num2, "is:", sum)
# print(f"The sum of {num1} and {num2} is: {sum}")


name = input("Enter your name: ")
hindi_marks = input("Enter Hindi Marks: ")
maths_marks = input("Enter Maths Marks ")
science_marks = input("Enter Science Marks ")

#perform operation
percentage = ((int(hindi_marks) +int(maths_marks) +int(science_marks))/300)*100
print(f"{name}, have {percentage}%. Well done & keep working hard !!")
