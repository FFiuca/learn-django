from rest_framework import serializers
from blog.models import Post
from blog.Models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    # post = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
        depth = 2

class PostSerializer(serializers.ModelSerializer):
    # category = serializers.SlugRelatedField(
    #     # many=True,
    #     read_only=True,
    #     slug_field='id'
    # )
    category = CategorySerializer(many=False, read_only=True)

    # category = serializers.PrimaryKeyRelatedField(read_only=True, many=False)

    class Meta:
        model = Post
        # fields = '__all__'
        exclude = []
        depth = 2
        # fields = ['id', 'title']

    # def __init__(self, instance=None, data=..., **kwargs):
    #     super().__init__(instance, data, **kwargs)
    #     self.Meta.depth = 2

class CategorySerializer2(serializers.ModelSerializer):
    post = PostSerializer(many=True, read_only=True)
    custom_field1 = serializers.SerializerMethodField(default='default')

    class Meta:
        model = Category
        fields = '__all__'
        depth = 1

    def get_custom_field1(self, instance):
        print('get_custom_field1', self.context, instance)
        return 'mboh'
