from rest_framework import serializers
from blog.models import Post
from blog.Models.category import Category

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = Category
        fields = '__all__'