from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
]

from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Correct update URL
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

# blog/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
]

# blog/urls.py
from django.urls import path
from .views import PostByTagListView  # Import the view that handles posts by tag

urlpatterns = [
    # Other URL patterns...
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),
]
