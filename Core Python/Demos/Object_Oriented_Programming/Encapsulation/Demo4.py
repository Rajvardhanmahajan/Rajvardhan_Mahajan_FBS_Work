class Farming:
    def __init__(self, farmid, farmName, location, ownerName):
        self.farmid = farmid
        self.farmName = farmName
        self.location = location
        self.ownerName = ownerName

    def getfarmid(self):
        return self.getfarmid
    def setfarmid(self, farmid):
        self.setfarmid = farmid

    def getfarmName(self):
        return self.farmName
    def setfarmName(self, farmname):
        self.setfarmName = farmname

    def getlocation(self):
        return self.location
    def setlocation(self, location):
        self.location = location

    def getOwnerName(self):
        return self.ownerName
    def setOwnerName(self, ownername):
        self.ownerName = ownername

    def display(self):
        print(f"farmid = {self.farmid}\t farmname = {self.farmName}\t location = {self.location}\t OwnerName = {self.ownerName}")

#Farming class is endss...

class DairyFarming(Farming):
    def __init__(self, farmid, farmName, location, ownerName, numberOfCattle, milkProduction):
        super().__init__(farmid, farmName, location, ownerName)
        self.numberOfCattle = numberOfCattle
        self.milkProduction = milkProduction

    def display(self):
        print(f"NoofCattle = {self.numberOfCattle} \t Milkproduction = {self.milkProduction}")
        return super().display()


#Main program 

f1 = DairyFarming(101, 'MahajanFarm', 'Anarad','YogeshwarMahajan', 5, 20)
f2 = Farming(102, 'MoreFarm', 'Nanded','Rajvardhan')
f3 = Farming(103, 'MahajanFarm', 'Shahada','Harshvardhan')

f1.display()
# f2.display()
# f3.display()