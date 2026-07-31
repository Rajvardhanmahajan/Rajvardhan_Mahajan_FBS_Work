# di = {'id':101, 'name':'rohit', 'sal': 75000}

# # di['sal'] = 100000

# di['salary'] = 100000

# print(di)


######
# emp = {'id': 123, 'name':'Sachin','sal':1234}

# for i,j in emp.items():
#     print(f'{i}:{j}')


######
# emp = {'id':1,'name':'Raj','sal':30000}
# emp['sal'] = emp['sal'] + emp['sal']*0.20

# print(emp)




######


emp = {}

for i in range(1, 4):
    name = input(f"Enter name of {i}th Employee: ")
    sal = int(input(f"Enter Salary{i}th : "))
    address = input(f"Enter Employee Address{i}: ")

    emp[i] = {
        "name": name,
        "sal": sal,
        "address": address
    }

print("\nEmployee Details:")

for i, j in emp.items():
    print(i, j)