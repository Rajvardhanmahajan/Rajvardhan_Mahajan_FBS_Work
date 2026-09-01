# 1. Create a class Complex Number with data members as real and imag and add
# following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

# Create ComplexNumber class
class ComplexNumber:

    # Parameterized constructor
    def __init__(self, real, imag):
        # Initialize real and imaginary parts
        self.real = real
        self.imag = imag

    # Destructor - called when object is destroyed
    def __del__(self):
        print("Object destroyed")

    # Operator overloading for + operator
    def __add__(self, other):
        return ComplexNumber(
            self.real + other.real,
            self.imag + other.imag
        )

    # Operator overloading for - operator
    def __sub__(self, other):
        return ComplexNumber(
            self.real - other.real,
            self.imag - other.imag
        )

    # Override __str__ method to display complex number
    def __str__(self):
        return f"{self.real} + {self.imag}i"


# Create first ComplexNumber object
c1 = ComplexNumber(10, 5)

# Create second ComplexNumber object
c2 = ComplexNumber(3, 2)


# Add two complex number objects
# Calls __add__() automatically
c3 = c1 + c2
print("Addition =", c3)


# Subtract two complex number objects
# Calls __sub__() automatically
c4 = c1 - c2
print("Substraction =", c4)