# Create Operation
Command:

from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

# Expected Output:
Book instance with title "1984" created successfully.

book = Book.objects.get(id=1)
print(book.title, book.author, book.publication_year)
