from ..serializers.post import PostSerializer
from blog.models import Post

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from rest_framework.permissions import IsAuthenticated
from .permission import IsAdminMixinOrAuthorOrReaderMixin

class PostCreateListAPIView(IsAdminMixinOrAuthorOrReaderMixin,ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    model = Post
    queryset = Post.objects.all()


class PostListAPIView(IsAdminMixinOrAuthorOrReaderMixin, ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    model = Post

    def get_queryset(self):
        return self.model.objects.filter(author = self.request.user, status = "published")

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        for obj in queryset:
            obj.views += 1
            obj.save()
        return super().list(request, *args, **kwargs)

class PostRetrieveUpdateDestroyAPIView(IsAdminMixinOrAuthorOrReaderMixin,RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    model = Post
    queryset = Post.objects.all()
    lookup_field = "id"
