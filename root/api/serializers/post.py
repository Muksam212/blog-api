from rest_framework import serializers
from blog.models import Post

from ..serializers.comments import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    # comments = CommentSerializer(many = True)
    id = serializers.IntegerField(read_only = True)
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "slug",
            "content",
            "author",
            "category",
            "status",
            "views"
        )