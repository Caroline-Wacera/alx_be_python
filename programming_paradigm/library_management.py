class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author):
        """Initialize a new book instance with title and author."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Check out the book, marking it as unavailable."""
        if self._is_checked_out:
            print(f"'{self.title}' is already checked out.")
        else:
            self._is_checked_out = True
            print(f"'{self.title}' has been checked out.")

    def return_book(self):
        """Return the book, marking it as available."""
        if not self._is_checked_out:
            print(f"'{self.title}' was not checked out.")
        else:
            self._is_checked_out = False
            print(f"'{self.title}' has been returned.")

    def is_available(self):
        """Return whether the book is available (not checked out)."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class representing the library that manages books."""

    def __init__(self):
        """Initialize an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        if not isinstance(book, Book):
            print("Only Book instances can be added to the library.")
        else:
            self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title, if available."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    return
                else:
                    print(f"'{title}' is currently unavailable.")
                    return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        for book in available_books:
            print(book)