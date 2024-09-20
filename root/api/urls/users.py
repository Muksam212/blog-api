from django.urls import path
from ..views.users import(
    UserRegisterView,
    UserListView,
    UserLoginView,
    UserPasswordResetAPIView,
    UserProfileListView
)

urlpatterns = [
    path('api/user/register/', UserRegisterView.as_view(), name = "api-user-register"),
    path('api/user/list/', UserListView.as_view(), name = "api-user-list"),
    path('api/user/login/', UserLoginView.as_view(), name = 'api-user-login'),
    path('api/user/password/reset/', UserPasswordResetAPIView.as_view(), name = 'api-user-password-reset'),
    path('api/user/profile/', UserProfileListView.as_view(), name = 'api-user-profile')
]
