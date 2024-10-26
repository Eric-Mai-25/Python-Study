class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        print(self.title + ', ' + self.author + ', ' + self.year + ' pewpew')
        return
    

book = Book("catcher" , "James", "1992")
book.display()