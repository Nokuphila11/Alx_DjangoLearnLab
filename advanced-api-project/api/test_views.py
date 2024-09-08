from django.test import TestCase
from rest_framework.test import APIClient
from .models import Book
from .serializers import BookSerializer

# Create an APIClient instance for making API requests
client = APIClient()

class BookTest(TestCase):
    def setUp(self):
        # Create a test Book object for use in tests
        self.book = Book.objects.create(title="Test Book", publication_year=2023, author=Author.objects.create(name="Test Author"))

    def test_create_book(self):
        # Prepare data for creating a new book
        data = {"title": "New Book", "publication_year": 2024, "author": self.book.author.id}

        # Make a POST request to create the book
        response = client.post('/api/books/', data=data, format='json')

        # Check for successful creation (status code 201)
        self.assertEqual(response.status_code, 201)

        # Deserialize the response data
        serialized_data = BookSerializer(data=response.data).data

        # Verify the created book data matches the request data
        self.assertEqual(serialized_data['title'], data['title'])
        self.assertEqual(serialized_data['publication_year'], data['publication_year'])

    # Add similar test cases for:
    # - Updating a Book
    # - Deleting a Book
    # - Filtering by author, publication year, etc.
    # - Searching for books by title
    # - Ordering books by different criteria
    # - Testing authorization and permissions for different user roles
