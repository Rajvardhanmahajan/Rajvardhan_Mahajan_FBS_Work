class Emp:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal
    def getId(self):
        return self.id
    def setId(self,id):
        self.id=id
    def getName(self):
        return self.name
    def setName(self, name):
        self.name=name
    def getSal(self):
        return self.sal
    def setSal(self, sal):
        self.sal = sal
    def calSal(self):
        print(f'Emp salary={self.sal}')
    def display(self):
        print(f'ID={self.id}\t name ={self.name} \t sal ={self.sal}')
#Emp class Ends Here...

    
#Main code ----->
e1=Emp(101,'Rajvardhan',4653)
e2=Emp(102,'Tanuja',44654)
e3=Emp(103,'Vidya',6546)
e4=Emp(104,'Aadinath',45564)
print(e3.getSal())
e2.setSal(6466889)
e2.display()
print(e4.getName())
e4.setName('Adinath')
print(e4.getName())
