#1. to pass multiple value to function
#2. Mention 1 asterisk symbol (*) before parameter name in function
#3. values will be stored in tuple.
#4. Use for loop it iterate values from tuple.

# def add(*num):
#     sum = 0
#     for val in num:
#         sum += val

#     return sum

# # res = add(10, 20, 30, 40, 50)
# num = tuple(map(int, input("Enter numbers separated by space: ").split()))
# res = add(*num)
# print('Addition is:', res)
# res = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# print('Addtion is:', res)



def mul(*num):
    mul = 1
    for val in num:
        mul *= val

    return mul

numbers = list(map(int, input('Enter numbers using space: ').split()))

res = mul(*numbers)
print('Multiplication: ', res)