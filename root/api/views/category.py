from ..serializers.category import CategorySerializer
from blog.models import Category

from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class CategoryCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    model = Category


class CategoryListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter
    queryset = Category.objects.all()


class CategoryUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    model = Category
    lookup_field = "id"
    queryset = Category.objects.all()