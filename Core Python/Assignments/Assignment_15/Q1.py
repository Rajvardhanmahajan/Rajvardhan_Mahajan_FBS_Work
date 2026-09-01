# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook

class Book:

    # Constructor (Supports Parameterized & Parameterless)
    def __init__(self, bid=0, bname="Not Available", price=0.0, author="Unknown"):
        self.__bid = bid
        self.__bname = bname
        self.__price = price
        self.__author = author


    # Show Book Details
    def showBook(self):
        print("\nBook ID :", self.__bid)
        print("Book Name :", self.__bname)
        print("Price :", self.__price)
        print("Author :", self.__author)
        

    # Destructor
    def __del__(self):
        print("Book Object Destroyed.")
# ---------------- Driver Code ----------------

# Parameterized Constructor
b1 = Book(101, "Python Programming", 550, "Pradip More")
b1.showBook()

print()

# Parameterless Constructor
b2 = Book()
b2.showBook()
