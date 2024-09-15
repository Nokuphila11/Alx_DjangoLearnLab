from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # Fields to be included in the form

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError('Title must be at least 5 characters long.')
        return title
# blog/forms.py
from django import forms
from django.contrib.auth.models import User

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

# forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include 'tags'

# forms.py
from django import forms
from .models import Post
from taggit.forms import TagWidget  # Import TagWidget for customizing tag input

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Make sure 'tags' is included
        widgets = {
            'tags': TagWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Add tags separated by commas',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your content here...',
            }),
        }
# widgets.py (Create a new file in your app)
from django.forms import TextInput

class "TagWidget()":
    def __init__(self, attrs=None):
        default_attrs = {'placeholder': 'Enter tags separated by commas'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

    def format_value(self, value):
        if value and hasattr(value, '__iter__'):
            return ', '.join([str(v) for v in value])
        return super().format_value(value)
