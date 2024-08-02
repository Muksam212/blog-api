from django.shortcuts import render

from rest_framework.generics import CreateAPIView
from .serializers import *
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }


class UserRegisterViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user":user,
            "msg": "Register Successful"
        }, status=status.HTTP_201_CREATED)
    

class UserLoginViewSet(ModelViewSet):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")

            usr = authenticate(username = username, password = password)
            if usr is not None:
                token = get_tokens_for_user(usr)
                return Response(token, status = status.HTTP_200_OK)
            else:
                return Response(
                    {
                        "details":"Username or Password Incorrect"
                    }, status = status.HTTP_404_NOT_FOUND
                )

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    

class UserProfileViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
    

class UserPasswordResetViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserPasswordChangeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = request.user
            serializer.update(user, serializer.validated_data)
            return Response({"msg": "Password reset successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileRegisterViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    model = Category
    queryset = Category.objects.all()



class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    model = Post
    queryset = Post.objects.all()