#1. To make parameter optional
#2. Assign value to parameter in function definition
#3.Flow is from right to left
#4. If we pass value to parameter in function call, it'll takes passed value
    #if we don't pass value to parameter in function call, it'll takes default value.

def emp(id, name, sal='50000', dept='Admin'):
    print('ID:', id)
    print('NAME:', name)
    print('SAL:',sal)
    print('DEPARTMENT:', dept)


emp(101, 'ABC', 35500, 'IT')
print('#####################')
emp(102, 'XYZ', 46500)
print('#####################')
emp(103, 'Raj')