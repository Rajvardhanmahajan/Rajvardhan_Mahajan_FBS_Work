class Book:
    def __init__(self, name, book_no, author, price):
        self.name = name
        self.book_no = book_no
        self.author = author
        self.price = price

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

    def getBook_NO(self):
        return self.book_no
    def setBook_NO(self, book_no):
        self.book_no = book_no

    def getauthor(self):
        return self.author
    def setauthor(self, author):
        self.author = author

    def getprice(self):
        return self.price
    def setprice(self, price):
        self.price = price

    def display(self):
        print(f"Name = {self.name} \t Book_No = {self.book_no} \t Author = {self.author} \t Price = {self.price}")

#Book class is ends here...

#Main program --->

b1 = Book('Python Crash Course', 785, 'Rajvardhan', 799)
b2 = Book('Java Book', 78995, 'Hanumant', 999)
b3 = Book('Networking Book', 789885, 'Ashish', 989)

b1.display()
print(b1.getauthor())

b1.setauthor('Harshvardhan')
print(b1.getauthor())


