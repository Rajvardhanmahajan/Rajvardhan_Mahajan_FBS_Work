#3. Python Program to Detect if Two Strings are Anagrams

def bubbleSort(character):
    size = len(character)

    for i in range(size - 1):
        for j in range(size - 1 - i):

            #compare adjacent characters
            if character[j] > character[j + 1]:
                character[j], character[j+1] = character[j+1], character[j]


def anagrams(text1, text2):

    #check if both strings have same length
    if len(text1) != len(text2):
        print('Strings are not Anagrams.')
        return

    #Convert strings into lists 
    list1 = list(text1)
    list2 = list(text2)

    #Sort both lists
    bubbleSort(list1)
    bubbleSort(list2)

    #compares both sorted lists
    if list1 == list2:
        print('Strings are Anagrams.')
    else:
        print('Strings are not Anagrams.')

    

text1 = 'listen'
text2 = 'silent'

anagrams(text1, text2)
