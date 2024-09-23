from ..serializers.comments import CommentSerializer
from blog.models import Comment
from rest_framework.generics import CreateAPIView, ListAPIView

from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response


class CommentCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    model = Comment


class CommentListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    model = Comment


class CommentAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        comment = Comment.objects.all().filter(user = user)
        serializer = CommentSerializer(comment, many = True)
        return Response(serializer.data)