from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()

    class Meta:
        ordering = ['created']

