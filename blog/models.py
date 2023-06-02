from django.db import models
from rest_framework import serializers
from django.utils.text import slugify
from datetime import datetime

from .models2 import Post2
from .Models import category
# from .forms.postForm import email_not_admin
# Create your models here.

class Post(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=False)
    email = models.EmailField(
            blank=True,
            null=True,
            validators=[
            #   email_not_admin
            ]
        )
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, editable=False)
    choice = models.CharField(max_length=255, blank=True, null=True, choices=[
        ('aku', 'aku'),
        ('kamu', 'kamu')
    ])

    # category = models.OneToOneField(
    #     category.Category,
    #     on_delete=models.CASCADE,
    # )

    # this for one to many relationship, will add column automatically, ex category_id
    category = models.ForeignKey(category.Category, on_delete=models.CASCADE, null=True, related_name='post')

    class Meta:
        permissions =(
            # (name, code)
            ('customer_pms_post', 'customer_pms_post2'),
            ('customer_pms_post3', 'customer_pms_post4'),
        )

    # override method from super/parent class, must include *args, **kwargs
    def save(self, *args, **kwargs):
        print(self)

        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        # print(self)
        return "{}, {}".format(self.title, self.body)


class Tag(models.Model):
    id= models.AutoField(primary_key=True)
    tag_name= models.CharField(blank=False, max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(blank=True, auto_now=True)

    def __str__(self):
        return "{}, {}".format(self.id, self.tag_name)


