# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.

# Shirt Management

class Shirt:

    # Static Variable (10% Price Increment)
    increment = 10

    # Constructor (Supports Parameterized & Parameterless)
    def __init__(self, sid=0, sname="Not Available", type="Formal", price=0.0, size="Small"):
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
        print("Original Price :", self.__price)
        print("Size :", self.__size)

    # Method to Calculate Price According to Size
    def calculatePrice(self):

        if self.__size.lower() == "small":
            finalPrice = self.__price

        elif self.__size.lower() == "medium":
            finalPrice = self.__price + (self.__price * Shirt.increment / 100)

        elif self.__size.lower() == "large":
            finalPrice = self.__price + (self.__price * 2 * Shirt.increment / 100)

        elif self.__size.lower() == "xlarge":
            finalPrice = self.__price + (self.__price * 3 * Shirt.increment / 100)

        else:
            finalPrice = self.__price

        print("Final Price :", finalPrice)

    # Destructor
    def __del__(self):
        print("Shirt Object Destroyed.")






# ---------------- Driver Code ----------------

# Parameterized Constructor
s1 = Shirt(101, "Arrow", "Formal", 1000, "large")

# Parameterless Constructor
s2 = Shirt()

# Display Shirt Details
s1.showShirt()

# Display Price According to Size
s1.calculatePrice()