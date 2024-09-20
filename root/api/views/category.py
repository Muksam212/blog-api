from ..serializers.category import CategorySerializer
from blog.models import Category

from rest_framework.generics import CreateAPIView, ListAPIView
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend

class CategoryCreateAPIView(CreateAPIView):
    serializer_class = CategorySerializer
    model = Category


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter
    model = Category
    queryset = Category.objects.all()