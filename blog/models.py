from django.db import models
from django.utils.text import slugify
from datetime import datetime

from .models2 import Post2
from .Models import category
# from .forms.postForm import email_not_admin
# Create your models here.

class Post(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField()
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

    category = models.OneToOneField(
        category.Category,
        on_delete=models.CASCADE,
    )

    # category = models.ForeignKey(category.Category, on_delete=models.CASCADE)

    class Meta:
        permissions =(
            ('customer_pms_post', 'customer_pms_post2'),
        )

    # override method from super/parent class, must include *args, **kwargs
    def save(self, *args, **kwargs):
        print(self)

        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        # print(self)
        return "{}, {}".format(self.title, self.body)


