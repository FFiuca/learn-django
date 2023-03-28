from django.db import models
from datetime import datetime

from .models2 import Post2
from .Models import category
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # print(self)
        return "{}".format(self.title)
