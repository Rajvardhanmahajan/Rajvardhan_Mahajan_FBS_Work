# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook

class Shirt:

    # Constructor (Supports Parameterized & Parameterless)
    def __init__(self, sid=0, sname="Not Available", type="Formal", price=0.0, size="Medium"):
        self.__sid = sid
        self.__sname = sname
        self.__type = type
        self.__price = price
        self.__size = size

    # Show Shirt Details
    def showShirt(self):
        print("\nShirt ID :", self.__sid)
        print("Shirt Name :", self.__sname)
        print("Type :", self.__type)
        print("Price :", self.__price)
        print("Size :", self.__size)

    # Destructor
    def __del__(self):
        print("Shirt Object Destroyed.")


# ---------------- Driver Code ----------------

# Parameterized Constructor
s1 = Shirt(101, "Arrow", "Formal", 1999, "Large")
s1.showShirt()

print()

# Parameterless Constructor
s2 = Shirt()
s2.showShirt()