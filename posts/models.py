import uuid
import os

from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    text = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, upload_to='post')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title