# Objective: Showcase inheritance with Book, EBook, PrintBook classes
#   and composition with a Library class managing books.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    def __init__(self):
        # self.base = Book()
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
