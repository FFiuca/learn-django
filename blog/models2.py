from django.db import models
from datetime import datetime

# Create your models here.

class Post2(models.Model):
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    email = models.EmailField(blank=True, null=True)
    category_id = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # print(self)
        return "{}".format(self.title)
