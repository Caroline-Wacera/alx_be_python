import os
import django

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")  # Change LibraryProject if your project has a different name
django.setup()

from relationship_app.models import Author, Book, Librarian

print("Django Query Samples Running...")

# Task 1: List all books in a library
def list_all_books():
    books = Book.objects.all()
    for book in books:
        print(book.title)

# Task 2: Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    if author:
        books = Book.objects.filter(author=author)
        for book in books:
            print(book.title)
    else:
        print("Author not found.")

# Task 3: Retrieve the librarian for a library
def librarian_for_library(library_name):
    librarian = Librarian.objects.filter(library__name=library_name).first()
    if librarian:
        print(f"Librarian: {librarian.name}")
    else:
        print("No librarian found for this library.")

# Run queries (for testing)
if __name__ == "__main__":
    list_all_books()
    books_by_author("J.K. Rowling")  # Example author
    librarian_for_library("Central Library")  # Example library