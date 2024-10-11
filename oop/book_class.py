class Book:
    def __init__(self, title , author , year):
        self.title = title 
        self.author = author 
        self.year = year      
    def __del__(self):
        Prints("Deleting title of the book upon object deletion.")
    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages."
    def __repr__(self):
        return f"Book('{self.title!r}', '{self.author!r}', {self.year!r})
