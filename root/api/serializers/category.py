from rest_framework import serializers
from blog.models import *

from ..serializers.post import PostSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id","name", "slug")
        depth = 1