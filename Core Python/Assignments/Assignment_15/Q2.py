# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook

class Product:

    # Constructor (Supports Parameterized & Parameterless)
    def __init__(self, pid=0, pname="Not Available", price=0.0, quantity=0):
        self.__pid = pid
        self.__pname = pname
        self.__price = price
        self.__quantity = quantity

    # Destructor
    def __del__(self):
        print("Product Object Destroyed.")

    # Show Product Details
    def showProduct(self):
        print("\nProduct ID :", self.__pid)
        print("Product Name :", self.__pname)
        print("Price :", self.__price)
        print("Quantity :", self.__quantity)


# ---------------- Driver Code ----------------

# Parameterized Constructor
p1 = Product(101, "Laptop", 55000, 1)
p1.showProduct()

print()

# Parameterless Constructor
p2 = Product()
p2.showProduct()