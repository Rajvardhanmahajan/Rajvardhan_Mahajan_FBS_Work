#Base class
class BusDriver:

    #Static variable
    depotName = "Pune depot"

    #constuctor
    def __init__(self, DriverID, DriverName, DriverLicense):
        self.__DriverID = DriverID
        self.__DriverName = DriverName
        self.__DriverLicense = DriverLicense

    #Static method
    @staticmethod
    def showDepot():
        print("\n Depot Name =", BusDriver.depotName)

    #Getter & setter for DriverId
    def getDriverID(self):
        return self.__DriverID
    def setDriverID(self,id):
        self.__DriverID = id

    #Getter & setter for DriverName
    def getDriverName(self):
        return self.__DriverName
    def setDriverName(self,name):
        self.__DriverName = name

    #Getter & setter for DriverLicense
    def getDriverLicense(self):
        return self.__DriverLicense
    def setDriverLicense(self,license):
        self.__DriverLicense = license

    #__str__() Method

    def __str__(self):
        return (f"DriverID = {self.__DriverID}\n"
                f"DriverName = {self.__DriverName}\n"
                f"DriverLicense = {self.__DriverLicense}\n")
#class Endss...

#Derieved class.

class ElectricBDriver(BusDriver):
    def __init__(self, DriverID, DriverName, DriverLicense,Experience):
        super().__init__(DriverID, DriverName, DriverLicense)
        self.__Experience = Experience

    def __str__(self):                                                                  #Not uses display method to display 
        return super().__str__() + f"Experience = {self.__Experience} years "           #To display object information in human readble form


#Objects 
print()
print(BusDriver.depotName)
print()
el1 = ElectricBDriver('E101','Ramakant',4754,5)
print(el1)
print()
b1 = BusDriver(101,'Ram',1232)
print(b1)