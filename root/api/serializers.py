from rest_framework import serializers
from users.models import *
from blog.models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
            "slug",
            "author",
            "category",
            "tags"
        )


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ("id","full_name", "username", "email", "password", "confirm_password")
        extra_kwargs = {
            "password":{"write_only": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError("Password didn't match")
        return attrs
        
    def create(self, validate_data):
        validate_data.pop("confirm_password", None)
        return User.objects.create_user(**validate_data)
    


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ("username", "password")


class UserProfileSerializer(serializers.ModelSerializer):
    user_posts = PostSerializer(many = True)
    class Meta:
        model = User
        fields = ("username",'email', "user_posts")
        depth = 2


class UserPasswordChangeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    confirm_password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ("password", "confirm_password")

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError("Password didn't match")
        return attrs
    

    def update(self, instance, validated_data):
        password = validated_data["password"]
        instance.set_password(password)
        instance.save()
        return instance
    

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("user", "bio")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id","name", "slug")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name", "slug")


