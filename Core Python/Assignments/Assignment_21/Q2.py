class Television:

    def __init__(self):
        self.modelNo = 0
        self.screenSize = 0
        self.price = 0

    def accept(self):
        self.modelNo = int(input("Enter Model Number: "))
        self.screenSize = float(input("Enter Screen Size: "))
        self.price = float(input("Enter Price: "))

        # Check Model Number
        if self.modelNo > 9999:
            raise ValueError("Model number cannot be more than 4 digits")

        # Check Screen Size
        if self.screenSize < 12 or self.screenSize > 70:
            raise ValueError("Screen size must be between 12 and 70 inches")

        # Check Price
        if self.price < 0 or self.price > 5000:
            raise ValueError("Price must be between 0 and 5000")

    def display(self):
        print("Model Number =", self.modelNo)
        print("Screen Size =", self.screenSize)
        print("Price =", self.price)


tv = Television()

try:
    tv.accept()
    tv.display()

except ValueError as e:
    print("Error:", e)

    # Replace all values with zero
    tv.modelNo = 0
    tv.screenSize = 0
    tv.price = 0

    print("\nData after exception:")
    tv.display()