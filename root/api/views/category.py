from ..serializers.category import CategorySerializer
from blog.models import Category

from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .permission import IsAdminMixinOrAuthorOrReaderMixin

class CategoryCreateAPIView(IsAdminMixinOrAuthorOrReaderMixin,CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    model = Category


class CategoryListAPIView(IsAdminMixinOrAuthorOrReaderMixin,ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter
    queryset = Category.objects.all()


class CategoryUpdateAPIView(IsAdminMixinOrAuthorOrReaderMixin,UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    model = Category
    lookup_field = "id"