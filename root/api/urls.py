from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserRegisterViewSet, 
    UserLoginViewSet,
    UserProfileViewSet,
    UserPasswordResetViewSet,
    ProfileRegisterViewSet,
    CategoryViewSet,
    PostViewSet
)

router = DefaultRouter()
router.register(r'users', UserRegisterViewSet, basename='user-register')
router.register(r'login', UserLoginViewSet, basename = 'user-login')
router.register(r'profile', UserProfileViewSet, basename='user-profile')
router.register(r'password/reset', UserPasswordResetViewSet, basename = 'user-reset')
router.register(r'profile/create', ProfileRegisterViewSet, basename = 'profile-register')
router.register(r'category/create', CategoryViewSet, basename = "category-create")
router.register(r'post', PostViewSet, basename = "post-create")

urlpatterns = [
    path('', include(router.urls)),
    # other paths
]