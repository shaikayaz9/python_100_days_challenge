# Exercise 6 ... 

# Write a libarry class with no_of_books and books as two instanc variable. write a program to create a library from this library class and show how yo can print all books. add books and get the number of books using different methods . show that your program doesnt persist the books after the program is stiooed!.


class Library:
    def __init__(self):
        self.noBooks= 0
        self.books = []

    def addBook(self,book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"the Library has {self.noBooks} books the books are")
        for book in self.books:
            print(book)


a = Library()
a.addBook("SPIDERMAN 1")
a.addBook("IRONMAN")
a.addBook("SPIDERMAN 2")
a.addBook("SPIDERMAN 3")
a.showInfo()
