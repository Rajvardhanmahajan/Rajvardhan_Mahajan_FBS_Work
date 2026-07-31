#11. WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.

# # Function to count digits
# def countdigit(num):
#     count = 0
#     temp = num

#     while temp > 0:
#         count += 1
#         temp = temp // 10

#     return count


# # Function to calculate Armstrong sum
# def armstrong(num, count):
#     total = 0
#     temp = num

#     while temp > 0:
#         digit = temp % 10
#         total = total + (digit ** count)
#         temp = temp // 10

#     return total

# #Taking input
# num = int(input("Enter Number: "))

# #Function call
# count = countdigit(num)

# result = armstrong(num, count)

# if result == num:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")