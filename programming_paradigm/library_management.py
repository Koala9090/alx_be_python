class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        self._books.append(book)
   
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False
    
    def list_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books available.")
