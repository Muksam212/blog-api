from .users import urlpatterns as users_urlpatterns
from .category import urlpatterns as category_urlpatterns
from .tag import urlpatterns as tag_urlpatterns
from .post import urlpatterns as post_urlpatterns

from django.urls import path, include

urlpatterns = [
    path('', include(users_urlpatterns)),
    path('', include(category_urlpatterns)),
    path('', include(tag_urlpatterns)),
    path('', include(post_urlpatterns))
]
