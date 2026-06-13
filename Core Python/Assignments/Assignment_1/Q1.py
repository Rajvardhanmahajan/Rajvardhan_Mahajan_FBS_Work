#1. Write a program to calculate the percentage of student based on marks of any 5 subjects.

#Take input
m1 = int(input('Subject1: '))
m2 = int(input('Subject2: '))
m3 = int(input('Subject3: '))
m4 = int(input('Subject4: '))
m5 = int(input('Subject5: '))

#Addition of all obtained marks.
Total = m1 + m2 + m3 + m4 + m5

#Operation
Percentage = (Total / 500) * 100

#Display result
print(f"Total marks obtained by student {Total} and it's marks in percentage is {Percentage} %.")