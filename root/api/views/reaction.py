from ..serializers.reaction import ReactionSerializer
from blog.models import Reaction

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import ListAPIView

class ReactionListCreateAPIView(ListCreateAPIView):
    serializer_class = ReactionSerializer
    model = Reaction
    queryset = Reaction.objects.all()


class ReactionRetrieveUpdateAPIVew(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReactionSerializer
    model = Reaction
    queryset = Reaction.objects.all()
    lookup_field = "id"


class ReactionListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReactionSerializer
    model = Reaction
    queryset = Reaction.objects.all()

    def get_queryset(self):
        return self.model.objects.filter(user = self.request.user)