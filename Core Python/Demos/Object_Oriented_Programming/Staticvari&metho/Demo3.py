# Static Method Example using Temperature

class Temperature:

    # Constructor
    def __init__(self, city):
        self.__city = city

    # Getter Method
    def getCity(self):
        return self.__city

    # Setter Method
    def setCity(self, city):
        self.__city = city

    # Display Method
    def display(self):
        print("City :", self.__city)

    # Static Method
    @staticmethod
    def celsiusToFahrenheit(celsius):
        fahrenheit = (celsius * 9/5) + 32
        print("Temperature in Fahrenheit :", fahrenheit)


# Driver Code
t = Temperature("Pune")
t.display()

print()

Temperature.celsiusToFahrenheit(25)



