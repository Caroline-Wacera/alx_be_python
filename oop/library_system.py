class Book:
    """Base class representing a book."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """String representation for Book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class for electronic books."""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in KB

    def __str__(self):
        """String representation for EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class for printed books."""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count  # Number of pages

    def __str__(self):
        """String representation for PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class to represent a collection of books."""
    def __init__(self):
        self.books = []  # List to store books

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        """List all books in the library."""
        for book in self.books:
            print(book)