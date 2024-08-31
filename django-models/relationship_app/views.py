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

 from django.views.generic import ListView
   from .models import Library  # Import your Library model

   class LibraryDetailView(ListView):
       model = Book
       template_name = 'relationship_app/library_detail.html'  # Create this template
       context_object_name = 'books'

       def get_queryset(self):
           library_id = self.kwargs['pk']  # Get the library ID from the URL
           return Book.objects.filter(library_id=library_id)  # Filter books by library
   



