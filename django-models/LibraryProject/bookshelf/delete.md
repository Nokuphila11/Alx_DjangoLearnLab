# Delete Operation
Command:

book.delete()
books = Book.objects.all()
print(books)

# Expected Output:
<QuerySet []> (Indicating no books are present in the database)

from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
