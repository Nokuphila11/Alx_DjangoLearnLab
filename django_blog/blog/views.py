from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Your list template
    context_object_name = 'posts'
    ordering = ['-published_date']  # Display newest posts first

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # Your detail template

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'  # Your create form template

    def form_valid(self, form):
        form.instance.author = self.request.user  # Automatically set the author
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only authors can edit their posts

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')  # Redirect to the post list after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure only authors can delete their posts

from django.contrib.auth.views import LoginView, LogoutView

# For login
class CustomLoginView(LoginView):
    template_name = 'blog/login.html'

# For logout
class CustomLogoutView(LogoutView):
    next_page = '/'
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Extend the UserCreationForm to include email field
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Register view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post-list')  # Redirect after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# blog/views.py
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, ProfileEditForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'registration/profile_edit.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'registration/profile.html')

def login_view(request):
    return auth_views.LoginView.as_view(template_name='registration/login.html')(request)

def logout_view(request):
    return auth_views.LogoutView.as_view(next_page='/')(request)
from django.db.models import Q
from django.shortcuts import render
from .models import Post

def search_posts(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) | 
            Q(tags__name__icontains=query)  # Search by tag name
        ).distinct()
    else:
        posts = Post.objects.all()
    
    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})

# views.py (in your blog app)
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import Comment, Post
from .forms import CommentForm

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'id': self.kwargs['post_id']})

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'

    def get_object(self, queryset=None):
        comment = super().get_object(queryset)
        if comment.author != self.request.user:
            raise PermissionDenied
        return comment

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'id': self.object.post.id})

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'

    def get_object(self, queryset=None):
        comment = super().get_object(queryset)
        if comment.author != self.request.user:
            raise PermissionDenied
        return comment

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'id': self.object.post.id})
