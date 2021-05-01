from django.db import models

from django.contrib.auth.models import User

from datetime import datetime


class Messages(models.Model):
    message = models.TextField(max_length=200)
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE, default=User.username)
    created = models.DateTimeField(default=datetime.now())
    target = models.ForeignKey(User, related_name='target', on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.message









