from ..views.tag import(
    TagCreateAPIView,
    TagListAPIView
)
from django.urls import path

urlpatterns = [
    path('api/tag/create/', TagCreateAPIView.as_view(), name = 'api-tag-create'),
    path('api/tag/list/', TagListAPIView.as_view(), name = 'api-tag-list')
]
