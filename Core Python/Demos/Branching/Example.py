#To  check the user login and password 
"""
pre_username = "Rajvardhan"
pre_password = "Raj@1234"

#Take inputs
username = input('Enter username: ')
password = input('Enter password: ')

#Excecution 
if (username == pre_username):
    if (password == pre_password):
        print('Congrats! Successfully login.')
    else:
        print('Password does not match.')
else:
    print('User name is not match.')"""


#Class example
username = 'admin'
password = '000' 

userid = input('Enter USERID:')
passw = input('Enter PASSWORD:')

if(username == userid and password == passw):
    print('Logged in successful.')
else:
    print('Invalid credentials.')