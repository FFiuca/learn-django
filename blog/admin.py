from django.contrib import admin

# This class purpose for manage admin django display, anything

# Register your models here.

from .models import Post, Tag
from .Models.category import Category


# this for setting for class model
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']

class TagAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']

# register your class model and his setting here
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
