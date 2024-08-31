from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# relationship_app/views.py
from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library  # Specify the model for the DetailView
    template_name = 'relationship_app/library_detail.html'  # Use this template to display the library details
    context_object_name = 'library'  # The context name used in the template


# relationship_app/views.py
from django.shortcuts import render
from django.views.generic.detail import DetailView  # Correct import for DetailView
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library  # Specify the model for the DetailView
    template_name = 'relationship_app/library_detail.html'  # Template to use for the view
    context_object_name = 'library'  # The context name used in the template



