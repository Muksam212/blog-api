from ..serializers.notification import NotificationSerializer
from blog.models import Notification

from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

class NotificationListCreateAPIView(ListCreateAPIView):
    serializer_class = NotificationSerializer
    # permission_classes = [IsAuthenticated]
    model = Notification
    queryset = Notification.objects.all()

class NotificationRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]


class NotificationListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer
    model = Notification
    queryset = Notification.objects.all()

    def get_queryset(self):
        return self.model.objects.filter(user = self.request.user)
