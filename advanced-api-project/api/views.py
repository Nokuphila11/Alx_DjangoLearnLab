from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# ListView to retrieve all books
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# DetailView to retrieve a single book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Overriding the create method to add custom behavior
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

    # Overriding the update method to add custom behavior
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    API view to retrieve a list of books.
    Unauthenticated users can access this view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a book by its ID.
    Unauthenticated users can access this view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    """
    API view to create a new Book.
    Only authenticated users can access this view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create

class BookUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing Book.
    Only authenticated use
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    API view to retrieve a list of books.
    - Filtering is supported by 'title', 'author', and 'publication_year'.
    - Searching is supported on 'title' and 'author' fields.
    - Ordering is available by 'title' and 'publication_year'.
    """
    ...

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters  # Correct import for DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    API view to retrieve a list of books.
    Allows filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users

    # Integrate filtering, searching, and ordering
    filter_backends = [filters.DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']  # Fields for filtering
    search_fields = ['title', 'author']  # Fields for search functionality
    ordering_fields = ['title', 'publication_year']  # Fields available for ordering
    ordering = ['title']  # Default ordering field

    from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter  # Correct import for OrderingFilter
from django_filters import rest_framework as filters  # Correct import for DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter  # Correct import for OrderingFilter
from django_filters import rest_framework as filters  # Import for DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    API view to retrieve a list of books.
    Allows filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users

    # Integrate filtering, searching, and ordering
    filter_backends = [filters.OrderingFilter] ["filters.SearchFilter"] # Correctly configured filter backends
    filterset_fields = ['title', 'aut


    # Integrate filtering, searching, and ordering
    filter_backends = [filters.DjangoFilterBackend, SearchFilter, OrderingFilter]  # Correctly configured filter backends
    filterset_fields = ['title', 'author', 'publication_year']  # Fields for filtering
    search_fields = ['title', 'author']  # Fields for search functionality
    ordering_fields = ['title', 'publication_year']  # Fields available for ordering
    ordering = ['title']  # Default ordering field


from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            publication_year=2024
        )
        self.url = '/api/books/'

    def test_create_book(self):
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'publication_year': 2025
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.latest('id').title, 'New Book')

    def test_read_book(self):
        response = self.client.get(self.url + f'{self.book.id}/')
        serializer = BookSerializer(self.book)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_book(self):
        data = {
            'title': 'Updated Book',
            'author': 'Updated Author',
            'publication_year': 2026
        }
        response = self.client.put(self.url + f'{self.book.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        response = self.client.delete(self.url + f'{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        response = self.client.get(self.url, {'title': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_search_books(self):
        response = self.client.get(self.url, {'search': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data['results']), 0)

    def test_ordering_books(self):
        response = self.client.get(self.url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that the results are ordered by publication_year

