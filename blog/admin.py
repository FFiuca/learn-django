from django.contrib import admin

# This class purpose for manage admin django display, anything

# Register your models here.

from .models import Post
from .Models.category import Category


# this for setting for class model
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']

# register your class model and his setting here
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
