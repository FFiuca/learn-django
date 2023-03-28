from django.db import models

# name class can anything, python can import with file name which must exactly match

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=30, blank=False)
