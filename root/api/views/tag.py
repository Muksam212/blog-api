from ..serializers.tag import TagSerializer
from blog.models import Tag

from rest_framework.generics import CreateAPIView, ListAPIView

class TagCreateAPIView(CreateAPIView):
    serializer_class = TagSerializer
    model = Tag


class TagListAPIView(ListAPIView):
    serializer_class = TagSerializer
    model = Tag
    queryset = Tag.objects.all()