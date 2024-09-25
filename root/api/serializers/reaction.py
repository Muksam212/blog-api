from rest_framework import serializers
from blog.models import Reaction

class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = (
            "id",
            "user",
            "post",
            "comment",
            "reaction"
        )