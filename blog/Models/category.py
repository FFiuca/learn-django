from django.db import models
from django.utils import timezone

# name class can anything, python can import with file name which must exactly match

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=30, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, auto_now=True, null=True)