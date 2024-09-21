from ..serializers.users import (
    UserRegisterSerializer,  
    UserListSerializer, 
    UserLoginSerializer,
    UserPasswordResetSerializer,
    UserProfileSerializer
)
from users.models import User

from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated

from .renderers import UserRenderers
from .filters import(
    UserFilter
)

from django_filters.rest_framework import DjangoFilterBackend

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }


class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer
    def post(self, request, format = None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user_data = self.serializer_class(user).data

            return Response(
                {"user": user_data, "msg": "Registration Success"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class UserListView(APIView):
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter  # Attach the filter class
    def get(self, request, format=None):
        # Get all users and apply filters
        user = User.objects.all()
        filterset = self.filterset_class(request.GET, queryset=user)  # Apply filters based on query params
        
        if filterset.is_valid():
            filtered_users = filterset.qs
            serializer = UserListSerializer(filtered_users, many=True)
            return Response(serializer.data)
        else:
            return Response(filterset.errors, status=400)

    
class UserLoginView(CreateAPIView):
    serializer_class = UserLoginSerializer
    renderer_classes = [UserRenderers]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data.get("username")
            password = serializer.data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response(token, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"detail": "username or password is not valid"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserPasswordResetAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserPasswordResetSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset = None):
        return self.request.user
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        # Return a custom response with message
        return Response({
            'message': 'Password has been reset successfully.'
        }, status=status.HTTP_200_OK)


class UserProfileListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format = None):
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)