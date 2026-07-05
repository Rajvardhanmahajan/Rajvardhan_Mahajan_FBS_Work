# #12. Write a program to check if given number is Armstrong number or not.
# # (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# # 4*4*4*4)

num = int(input('Enter the Number: '))

temp = num

count = 0

while num > 0:
    count += 1
    num = num // 10
   

num = temp

total = 0

while num > 0:
    digit = num % 10
    total = total + (digit ** count)
    num = num // 10

if temp == total:
    print(f'This is armstrong number.')
else:
    print(f'This is not armstrong number.')



#To find armstrong Number from given range. 

# #Take input as start and end value.
# start = int(input('Enter the number: '))
# end = int(input('Enter the end number: '))

# #create range 
# for num in range(start, end+1):


#     temp = num      

#     count = 0

#     while num > 0:
#         num = num // 10
#         count += 1


#     num = temp

#     total = 0

#     while num > 0:
#         d = num % 10
#         total = total + (d ** count)
#         num = num // 10

#     if temp == total:
#         print(temp)