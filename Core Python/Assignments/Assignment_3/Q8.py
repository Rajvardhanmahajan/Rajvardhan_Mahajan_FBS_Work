#8. Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha)

import random
captcha = random.randint(1000, 9999)

Pre_username = 'Rajvardhan'
Pre_password = 'Raj@123'

#Take inputs
username = input('Enter username: ')
password = input('Enter password: ')

if (username == Pre_username) and (password == Pre_password):
    print('Captcha =', captcha)

    user_captcha = int(input('Enter the Captcha: '))

    if (user_captcha == captcha):
        print('Login Successful.')
    else:
        print('Captcha Verification Failed.')

else:
    print('Invalid Username or Password!!')

