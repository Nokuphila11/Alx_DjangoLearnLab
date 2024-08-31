# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # URL for function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for class-based view
]

# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView, login, logout, register

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', login, name='login'),  # URL for login view
    path('logout/', logout, name='logout'),  # URL for logout view
    path('register/', register, name='register'),  # URL for registration view
]
