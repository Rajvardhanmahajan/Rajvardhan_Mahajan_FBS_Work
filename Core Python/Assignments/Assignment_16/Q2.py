# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.

class Product:

    # Static Variable
    discount = 10      # 10% Discount

    # Constructor (Supports Parameterized & Parameterless)
    def __init__(self, pid=0, pname="Not Available", price=0.0, quantity=0):
        self.__pid = pid
        self.__pname = pname
        self.__price = price
        self.__quantity = quantity

    # Show Product Details
    def showProduct(self):
        print("\nProduct ID :", self.__pid)
        print("Product Name :", self.__pname)
        print("Price :", self.__price)
        print("Quantity :", self.__quantity)

    # Method to Apply Discount
    def applyDiscount(self):
        discountAmount = (self.__price * Product.discount) / 100
        finalPrice = self.__price - discountAmount
        print("Price After Discount :", finalPrice)

    # Destructor
    def __del__(self):
        print("Product Object Destroyed.")


# ---------------- Driver Code ----------------

# Parameterized Constructor
p1 = Product(101, "Laptop", 60000, 5)

# Parameterless Constructor
p2 = Product()

# Display Product Details
p1.showProduct()
p2.showProduct()

# Apply Discount
p1.applyDiscount()