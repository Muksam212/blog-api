from ..views.comments import CommentCreateAPIView
from django.urls import path

urlpatterns = [
    path('api/comments/create/', CommentCreateAPIView.as_view(), name = 'api-comment-create')
]
