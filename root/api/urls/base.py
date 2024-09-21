from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions



from .users import urlpatterns as users_urlpatterns
from .category import urlpatterns as category_urlpatterns
from .tag import urlpatterns as tag_urlpatterns
from .post import urlpatterns as post_urlpatterns
from .comments import urlpatterns as comments_urlpatterns

from django.urls import path, include

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version="v1",
        description="API Swagger",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="info@asparksys.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = (
    [
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
        ),
    ]
    +users_urlpatterns
    +category_urlpatterns
    +tag_urlpatterns
    +comments_urlpatterns
    +post_urlpatterns
)
