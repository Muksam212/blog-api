from ..views.reaction import ReactionListCreateAPIView, ReactionRetrieveUpdateAPIVew, ReactionListAPIView
from django.urls import path

urlpatterns = [
    path('api/reaction/list/create/', ReactionListCreateAPIView.as_view(), name = 'api-reaction-list-create'),
    path('api/reaction/retrieve/<int:id>/', ReactionRetrieveUpdateAPIVew.as_view(), name = 'api-reaction-retrieve'),
    path('api/reaction/list/', ReactionListAPIView.as_view(), name = 'api-reaction-list')
]
