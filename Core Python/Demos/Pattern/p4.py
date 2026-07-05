#for print A A A A A
#          B B B B B

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(chr(64 + i), end=' ')
#     print()



# for i in range(1, 6):
#     for j in range(1, i +1):
#         print(chr(64 + i), end=' ')
#     print()



for i in range(1, 6):
    for j in range(1, i +1):
        print(chr(64 + j), end=' ')
    print()

   


# for i in range(1, 6):
#     for j in range(1, 7-i):
#         print(chr(64 + i), end=' ')
#     print()