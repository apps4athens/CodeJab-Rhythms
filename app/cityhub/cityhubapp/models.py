from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class UserInterest(models.Model):
    value = models.CharField(max_length=50)

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('cityzen', 'Δημότης'),
        ('mayor', 'Δήμαρχος'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    municipality = models.CharField(max_length=100)
    brief = models.CharField(max_length=300)
    interests = models.ManyToManyField(UserInterest, blank=True)

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    POST_TYPES = (
        ('event', 'Δράση'),
        ('complaint', 'Παράπονο')
    )
    type = models.CharField(max_length=20, choices=POST_TYPES)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    published_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Like(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=200)
