from django.db import models
from django.utils.text import slugify
from datetime import datetime

from .models2 import Post2
from .Models import category
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, editable=False)

    # override method from super/parent class
    def save(self):
        print(self)

        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        # print(self)
        return "{}".format(self.title)

