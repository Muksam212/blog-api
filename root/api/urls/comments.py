from ..views.comments import (
    CommentCreateAPIView,
    CommentListAPIView, 
    CommentAPIView
)
from django.urls import path

urlpatterns = [
    path('api/comments/create/', CommentCreateAPIView.as_view(), name = 'api-comment-create'),
    path('api/comments/list/', CommentListAPIView.as_view(), name = 'api-comment-list'),
    path('api/comments/list/specify/', CommentAPIView.as_view(), name = 'api-comment-list-specify')
]
