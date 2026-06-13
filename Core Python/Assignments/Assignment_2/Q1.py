#1. Convert the time entered in hh,min and sec into seconds.

#Take input

hh = int(input('Enter hour: '))
min = int(input('Enter minute: '))
sec = int(input('Enter second: '))

#Perform operation
Total_sec = (hh * 3600) + (min * 60) + sec

#Display result
print(f'The converted seconds is {Total_sec}.')