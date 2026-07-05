#2. Write a program to input any alphabet and check whether it is vowel or consonant.

#Take input
Alpha = input('Enter Alphabets: ')

#Perform operation
if (Alpha in 'aeiouAEIOU'):    # in - is a membership operator. Define - part or phrase present in given list or sequence.
    print('It is vowel.')
else:
    print('It is consonant.')