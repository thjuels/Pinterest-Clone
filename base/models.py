from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Pin(models.Model):
    
    pinner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)#anytime the model is updated, it will be saved
    created = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(default='avatar.svg')#null=False, default= ## add parameters later
    
    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return self.name