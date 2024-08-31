from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Book
from .forms import BookForm

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'view_book.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'confirm_delete.html', {'book': book})

from django.shortcuts import render
from .models import Book
from django.db.models import Q

def search_books(request):
    query = request.GET.get('q', '')
    if query:
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

