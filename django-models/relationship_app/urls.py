# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL for function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for class-based view
]

from django.urls import path

from . import views  # Import the views.py file from the current directory

urlpatterns = [
  path('login/', views.login_view, name='login'),
  path('logout/', views.logout_view, name='logout'),
  path('register/', views.register_view, name='register'),
]

]

# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView, register  # Ensure 'register' is imported
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),  # Ensure 'register' view is linked here
]

# relationship_app/urls.py
from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]

# relationship_app/urls.py
from django.urls import path
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path('add-book/', add_book, name='add_book'),
    path('edit-book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete-book/<int:book_id>/', delete_book, name='delete_book'),
]

# relationship_app/urls.py
from django.urls import path
from .views import add_book, edit_book, delete_book

urlpatterns = [
    # URL pattern for adding a book
    path('add-book/', add_book, name='add_book'),
    
    # URL pattern for editing a book
    path('edit-book/<int:book_id>/', edit_book, name='edit_book'),
    
    # URL pattern for deleting a book
    path('delete-book/<int:book_id>/', delete_book, name='delete_book'),
]
