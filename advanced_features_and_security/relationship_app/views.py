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

# relationship_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Login view
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirect to a home page or any other page
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# Logout view
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('login')  # Redirect to the login page after logout
    return render(request, 'relationship_app/logout.html')

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

from django.contrib.auth.decorators import user_passes_test

def admin_view(request):
    # Only accessible to users with the 'Admin' role
    return render(request, 'admin_template.html')

def librarian_view(request):
    # Only accessible to users with the 'Librarian' role
    return render(request, 'librarian_template.html')

def member_view(request):
    # Accessible to users with the 'Member' role
    return render(request, 'member_template.html')


@user_passes_test(lambda u: u.profile.role == 'Admin')
def admin_view(request):
    # ...

@user_passes_test(lambda u: u.profile.role == 'Librarian')
def librarian_view(request):
    # ...

@user_passes_test(lambda u: u.profile.role == 'Member')
def member_view(request):
    # ...
# relationship_app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import UserProfile

# Helper function for role-based access
def user_is_admin(user):
    return user.userprofile.role == 'Admin'

def user_is_librarian(user):
    return user.userprofile.role == 'Librarian'

def user_is_member(user):
    return user.userprofile.role == 'Member'

# Admin View
@user_passes_test(user_is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian View
@user_passes_test(user_is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# relationship_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import View
from .models import Book

# View to Add a New Book
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        # Assume Author model exists and is imported
        author = get_object_or_404(Author, pk=author_id)
        Book.objects.create(title=title, author=author, publication_year=publication_year)
        return redirect('book_list')
    return render(request, 'relationship_app/add_book.html')

# View to Edit a Book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author_id = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return redirect('book_list')
    return render(request, 'relationship_app/edit_book.html', {'book': book})

# View to Delete a Book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})


# Member View
@user_passes_test(user_is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
