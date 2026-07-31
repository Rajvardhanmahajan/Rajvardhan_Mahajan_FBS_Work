#1.To neglate positional parameter concept.
#2.Flow right to left.
#3.Assign value in function call
#4.To pass argument is any order.
#5.Keyword arguments are passed using parameter names.


def emp(id, name, sal, dept, mobile_no, email, age, adhar):
    data = f'ID:{id}\nNAME:{name}\nSAL:{sal}\nDEPT:{dept}\nMOBILE_NO:{mobile_no}\nEMAIL:{email}\nAGE:{age}\nADHAR:{adhar}'
    return data

res = emp(101, sal=35000,  name='ABC', dept='IT', age = 22, adhar= 805056, mobile_no= 8010586823, email='raj@gmail.com')
print(res)
print("**********************")

print(res)