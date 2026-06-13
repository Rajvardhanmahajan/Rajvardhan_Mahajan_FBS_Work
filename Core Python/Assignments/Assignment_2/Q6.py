#6. WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.

#Take input
Basic = int(input('Enter basic salary: '))


#Operation
da = (Basic * 10) / 100
ta = (Basic * 12) / 100
hra = (Basic * 15) / 100

Total_salary = Basic + da + ta + hra

#Display result
print(f'The Total Salary of employee is {int(Total_salary)}.')
