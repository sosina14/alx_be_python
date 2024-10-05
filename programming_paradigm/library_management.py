class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is available, False otherwise."""
        return not self._is_checked_out

class Library:
    """A class representing a library, which manages a collection of books."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a book to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it's available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out: {book.title} by {book.author}")
                return
        print(f"Sorry, the book '{title}' is not available.")

    def return_book(self, title):
        """Return a book by title to make it available again."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned: {book.title} by {book.author}")
                return
        print(f"The book '{title}' was not checked out.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
