from rest_framework import serializers
from blog.models import *

from ..serializers.post import PostSerializer

class CategorySerializer(serializers.ModelSerializer):
    category_post = PostSerializer(many = True)
    class Meta:
        model = Category
        fields = ("id","name", "slug", "category_post",)
        depth = 1