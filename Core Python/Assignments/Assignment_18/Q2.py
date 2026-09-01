# 2. Create a class Distance with data members as km,m and cm and add following
# methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

# Create Distance class
class Distance:

    # Parameterized constructor
    def __init__(self, km, m, cm):
        # Initialize kilometer, meter and centimeter
        self.km = km
        self.m = m
        self.cm = cm

    # Destructor - called when object is destroyed
    def __del__(self):
        print("Object destroyed")

    # Operator overloading for + operator
    def __add__(self, other):

        # Convert both distances into centimeters
        total_cm = (
            (self.km * 100000 + self.m * 100 + self.cm)
            + (other.km * 100000 + other.m * 100 + other.cm)
        )

        # Convert total centimeters back into km, m and cm
        km = total_cm // 100000
        total_cm %= 100000

        m = total_cm // 100
        cm = total_cm % 100

        # Return a new Distance object
        return Distance(km, m, cm)

    # Operator overloading for - operator
    def __sub__(self, other):

        # Convert both distances into centimeters and subtract
        total_cm = (
            (self.km * 100000 + self.m * 100 + self.cm)
            - (other.km * 100000 + other.m * 100 + other.cm)
        )

        # Convert total centimeters back into km, m and cm
        km = total_cm // 100000
        total_cm %= 100000

        m = total_cm // 100
        cm = total_cm % 100

        # Return a new Distance object
        return Distance(km, m, cm)

    # Override __str__ method to display distance
    def __str__(self):
        return f"{self.km} km {self.m} m {self.cm} cm"


# Create first Distance object
d1 = Distance(5, 20, 50)

# Create second Distance object
d2 = Distance(2, 30, 75)


# Add two Distance objects
# Calls __add__() automatically
d3 = d1 + d2
print("Addition =", d3)


# Subtract two Distance objects
# Calls __sub__() automatically
d4 = d1 - d2
print("Subtraction =", d4)