from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)  # Adjust length as needed

class Book(models.Model):
    title = models.CharField(max_length=255)  # Adjust length as needed
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Author deletion cascades to books

class Library(models.Model):
    name = models.CharField(max_length=255)  # Adjust length as needed
    books = models.ManyToManyField(Book)  # Many books can belong to many libraries

class Librarian(models.Model):
    name = models.CharField(max_length=255)  # Adjust length as needed
    library = models.OneToOneField(Library, on_delete=models.CASCADE)  # One-to-one relationship with a library
