from .users import urlpatterns as users_urlpatterns
from .category import urlpatterns as category_urlpatterns

from django.urls import path, include

urlpatterns = [
    path('', include(users_urlpatterns)),
    path('', include(category_urlpatterns))
]
