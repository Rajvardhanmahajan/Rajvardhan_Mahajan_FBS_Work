def emp(**data):
   # print(type(data))
    # print(data)
    for key, val in data.items():
        print(f'{key}: {val}')
    return data


# emp(id=101, name='ABC', sal=50000, dept='IT',mobile='801059',email='raj@gmail.com',adhar=789698)

res = emp(id=101, name='ABC', sal=50000, dept='IT',mobile='801059',email='raj@gmail.com',adhar=789698)
print(res)
