class Library:
    def __init__(self):
        self.nobooks = 0
        self.books = []

    def addbooks(self, book):
        self.books.append(book)
        self.nobooks = len(self.books)

    def showinfo(self):
        print(f"The Library has {self.nobooks} books. The books are : ")
        for book in self.books:
            print(book)


l1 = Library()
l1.addbooks("Harry Potter")
l1.addbooks("Demon's bell")
l1.addbooks("The new Era")
l1.showinfo()
