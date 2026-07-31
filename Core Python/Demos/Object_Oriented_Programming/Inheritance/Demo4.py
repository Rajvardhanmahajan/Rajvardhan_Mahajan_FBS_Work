# Multiple Inheritance

class Teacher:

    def __init__(self, subject):
        self.__subject = subject

    def getSubject(self):
        return self.__subject

    def setSubject(self, subject):
        self.__subject = subject

    def displayTeacher(self):
        print("Subject :", self.__subject)


class Researcher:

    def __init__(self, field):
        self.__field = field

    def getField(self):
        return self.__field

    def setField(self, field):
        self.__field = field

    def displayResearch(self):
        print("Research Field :", self.__field)


class Professor(Teacher, Researcher):

    def __init__(self, subject, field):
        Teacher.__init__(self, subject)
        Researcher.__init__(self, field)

    def display(self):
        self.displayTeacher()
        self.displayResearch()


p = Professor("Python", "Artificial Intelligence")
p.display()