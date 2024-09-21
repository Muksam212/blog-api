from ..serializers.comments import CommentSerializer
from blog.models import Comment
from rest_framework.generics import CreateAPIView


class CommentCreateAPIView(CreateAPIView):
    serializer_class = CommentSerializer
    model = Comment