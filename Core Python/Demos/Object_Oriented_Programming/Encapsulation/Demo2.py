#Hospital management using Encapsulation

class Hospital:
    #constructor
    def __init__(self,patientId, name, disease, roomNO):
        self.__patientId = patientId
        self.__name = name
        self.__disease = disease 
        self.__roomNO = roomNO

    #Getter & setter for patientId
    def getPatientID(self):
        return self.__patientId 
    def setPatientID(self,id):
        self.__patientId = id

    #Getter & setter for name
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name = name

    #Getter & setter for disease
    def getdisease(self):
        return self.__disease
    def setdisease(self,disease):
        self.__disease = disease

    #Getter & setter for roomNo
    def getroomNO(self):
        return self.__roomNO
    def setroomNO(self,roomNo):
        self.__roomNO = roomNo

    #Display method
    def display(self):
        print("Patient ID :", self.__patientId)
        print("Patient Name :", self.__name)
        print("Disease :", self.__disease)
        print("Room No :", self.__roomNO)

#Class endss... 

#Object 
h = Hospital(101,'Ram','Fever',12)

print('Before Update')
h.display()

#Updating data using setter 
h.setdisease('Typhoid')
h.setroomNO(15)

print('\nAfter Update')
h.display()