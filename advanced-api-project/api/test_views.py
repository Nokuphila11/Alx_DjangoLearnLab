from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from rest_framework import status  # Import status codes
from .models import Book
from .serializers import BookSerializer

# Create an APIClient instance for making API requests
client = APIClient()

class BookTest(APITestCase):

    def setUp(self):
        # Create a test Book object for use in tests
        self.book = Book.objects.create(title="Test Book", publication_year=2023, author=Author.objects.create(name="Test Author"))

    def test_create_book(self):
        # Prepare data for creating a new book
        data = {"title": "New Book", "publication_year": 2024, "author": self.book.author.id}

        # Make a POST request to create the book
        response = self.client.post('/api/books/', data=data, format='json')

        # Check for successful creation (status code 201)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Use status.HTTP_201_CREATED

        # Deserialize the response data
        serialized_data = BookSerializer(data=response.data).data

        # Verify the created book data matches the request data
        self.assertEqual(serialized_data['title'], data['title'])
        self.assertEqual(serialized_data['publication_year'], data['publication_year'])

    # Add similar test cases using self.client
def test_update_book_authenticated(self):
    # Login a user (replace with your user credentials)
    self.client.login(username="test_user", password="test_password")

    # Prepare data for updating the book
    data = {"title": "Updated Book Title"}

    # Make a PUT request with authentication
    response = self.client.put('/api/books/1/', data=data, format='json')

    # Check for successful update (status code 200)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

    # ... further assertions on the updated data
