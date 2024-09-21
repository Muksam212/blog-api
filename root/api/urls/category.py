from ..views.category import (
    CategoryCreateAPIView,
    CategoryListAPIView,
    CategoryUpdateAPIView
)
from django.urls import path

urlpatterns = [
    path('api/category/create/', CategoryCreateAPIView.as_view(), name = "api-category-create"),
    path('api/category/list/', CategoryListAPIView.as_view(), name = 'api-category-list'),
    path('api/category/update/<int:id>/', CategoryUpdateAPIView.as_view(), name = 'api-category-update')
]
