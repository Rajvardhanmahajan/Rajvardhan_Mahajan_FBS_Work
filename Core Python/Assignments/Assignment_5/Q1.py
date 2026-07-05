# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

preuserid = 'Rajvardhan'
prepass = 'Raj@321'

# count = 0

# while count < 3:
#     userid = input('Enter username: ')
#     password = input('Enter password: ')

#     if (userid == preuserid) and (prepass == password):
#         print('Login successful!')
#         break

#     else:
#         print('Envalid username or password!')
#         count = count + 1

# else:
#     print('Program terminated!')


#Program using for loop 

for i in range(1, 4):   #Itration value 1 2 3 

    userid = input('Enter username: ')
    password = input('Enter password: ')

    
    if (userid == preuserid) and (prepass == password):
        print('Login successful!')
        break

    else:
        print('Envalid Password or Userid!')

else:
    print('Program Terminated!')

