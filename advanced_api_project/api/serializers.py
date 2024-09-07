from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']  # Fields to be serialized

    # Custom validation for publication_year
    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serialization for books

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

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
