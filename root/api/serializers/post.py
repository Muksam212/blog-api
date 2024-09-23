from rest_framework import serializers
from blog.models import Post

from ..serializers.comments import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer()
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "slug",
            "content",
            "author",
            "category",
            "tags",
            "status",
            "views",
            "comments"
        )
        depth = 1