from ..views.post import (
    PostCreateListAPIView,
    PostRetrieveUpdateDestroyAPIView,
    PostListAPIView,
)
from django.urls import path

urlpatterns = [
    path('api/post/create/', PostCreateListAPIView.as_view(), name = 'api-post-create'),
    path('api/post/update/<int:id>/', PostRetrieveUpdateDestroyAPIView.as_view(), name = 'api-post-update'),
    path('api/post/retrieve/', PostListAPIView.as_view(), name = 'api-post-retrieve')
]
