import django_filters
from users.models import User

from blog.models import *

class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name="username", lookup_expr="iexact")
    role = django_filters.CharFilter(field_name="role", lookup_expr="iexact")
    class Meta:
        model = User
        fields = ("username", "role")


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name = "name", lookup_expr="iexact")
    slug = django_filters.CharFilter(field_name="slug", lookup_expr="iexact")

    class Meta:
        model = Category
        fields = ("name", "slug")