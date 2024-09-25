from ..views.notification import (
    NotificationListCreateAPIView,
    NotificationRetrieveUpdateView,
    NotificationListAPIView
)
from django.urls import path

urlpatterns = [
    path('api/notification/list/create/', NotificationListCreateAPIView.as_view(), name = 'api-notification-list-create'),
    path('notifications/<int:pk>/', NotificationRetrieveUpdateView.as_view(), name='notification-detail'),
    path('notification/retrieve/', NotificationListAPIView.as_view(), name = 'notification-retrieve')
]
