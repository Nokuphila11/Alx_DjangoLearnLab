# api/urls.py

from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create a router and register the BookViewSet with it
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token  # Import token view
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token auth endpoint
]
