from ..views.category import (
    CategoryCreateAPIView,
    CategoryListAPIView
)
from django.urls import path

urlpatterns = [
    path('api/category/create/', CategoryCreateAPIView.as_view(), name = "api-category-create"),
    path('api/category/list/', CategoryListAPIView.as_view(), name = 'api-category-list')
]
