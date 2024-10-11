# Base Class - Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"Book: {self.title} by {self.author}"

# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        # Instead of using super(), call the Book class directly
        Book.__init__(self, title, author)  # Initialize parent class attributes
        self.file_size = file_size  # Unique to EBook

    def get_info(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call the Book class directly to initialize inherited attributes
        Book.__init__(self, title, author)  # Initialize parent class attributes
        self.page_count = page_count  # Unique to PrintBook

    def get_info(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Composition - Library
class Library:
    def __init__(self):
        self.books = []  # List to store Book instances

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Error: Only Book instances can be added to the library.")

    def list_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            for book in self.books:
                print(book.get_info())
