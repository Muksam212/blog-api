from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class IsAdminMixinOrAuthorOrReaderMixin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['Admin', 'Author', 'Reader']
    