from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
