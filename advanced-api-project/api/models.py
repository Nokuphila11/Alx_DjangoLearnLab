from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)  # Author's name field

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)  # Book's title field
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # Foreign key to Author

    def __str__(self):
        return self.title

from api.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer

# Create an Author instance
author = Author.objects.create(name='J.K. Rowling')

# Create a Book instance
book = Book.objects.create(title='Harry Potter', publication_year=1997, author=author)

# Serialize an Author instance
author_serializer = AuthorSerializer(author)
print(author_serializer.data)

# Serialize a Book instance
book_serializer = BookSerializer(book)
print(book_serializer.data)
