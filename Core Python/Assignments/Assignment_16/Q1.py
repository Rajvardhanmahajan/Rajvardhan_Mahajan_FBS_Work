# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.

class Book:

    # Static Variable
    count = 0

    # Constructor (Supports Parameterized & Parameterless)
    def __init__(self, bid=0, bname="Not Available", price=0.0, author="Unknown"):
        self.__bid = bid
        self.__bname = bname
        self.__price = price
        self.__author = author

        # Increment Static Variable whenever an object is created
        Book.count += 1

    # Show Book Details
    def showBook(self):
        print("\nBook ID :", self.__bid)
        print("Book Name :", self.__bname)
        print("Price :", self.__price)
        print("Author :", self.__author)

    # Destructor
    def __del__(self):
        print("Book Object Destroyed.")

    # Static Method to Display Object Count
    @staticmethod
    def showCount():
        print("\nTotal Objects Created =", Book.count)


# ---------------- Driver Code ----------------

# Creating Objects
b1 = Book(101, "Python", 450, "Pradip More")
b2 = Book(102, "Java", 550, "James Gosling")
b3 = Book()

# Display Book Details
b1.showBook()
b2.showBook()
b3.showBook()

# Display Total Objects Created
Book.showCount()