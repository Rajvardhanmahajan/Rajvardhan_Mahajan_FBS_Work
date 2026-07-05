#7. Write a program to check if user has entered correct userid and password.

pre_user = 'Rajvardhan'
pre_pass = 'Raj#321'

#Take input
userid = input('Enter Userid: ')
password = input('Enter Password: ')

# if (userid == pre_user):
    # if (password == pre_pass):
        # print('Login successful!')
    # else:
        # print('Envalid Password!')
# else:
    # print('Invalid Userid!')


if (userid == pre_user) and (password == pre_pass):
    print('Login successful!')
else:
    print('Envalid Credentials!')