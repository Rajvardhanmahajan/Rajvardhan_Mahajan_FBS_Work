#9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

#Take input
Math = int(input('Enter Marks of Mathematics:  '))
Sci = int(input('Enter Marks of Science: '))
Phy = int(input('Enter Marks of Physics: '))
Che = int(input('Enter Marks of Chemistry: '))
Eng = int(input('Enter Marks of English: '))


#Perform operation

Total = Math + Sci + Phy + Che + Eng 

percentage = (Total / 500) * 100

if (percentage > 90):
    print(f'A+ Class {percentage}%.')
elif (percentage > 80):
    print(f'A Class {percentage}%.')
elif (percentage > 70):
    print(f'First Class {percentage}%.')
elif (percentage > 60):
    print(f'Second Class {percentage}%.')
elif (percentage > 50):
    print(f'Third Class {percentage}%.')
else:
    print(f'Fail {percentage}%.')