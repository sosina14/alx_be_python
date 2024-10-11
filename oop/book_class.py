# book_class.py:
class Book:
    def __init__(self, title , author , year):
        self.title = title 
        self.author = author 
        self.year = year
        
    def __del__(self):
         Prints ("Deleting title of the book upon object deletion.")
         
"""String Representation (__str__): Returns a string in the format "(title) by (author), published in (year)"."""

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."
        
"""Official Representation (__repr__): Returns a string that would recreate the Book instance: f"Book('{self.title}', '{self.author}', {self.year})"""

    def __repr__(self):
        return f"Book('{self.title!r}', '{self.author!r}', {self.year!r})
