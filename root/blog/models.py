from django.db import models

from root.utils import BaseModel
from users.models import User
# Create your models here.

class Category(BaseModel):
    name = models.CharField(max_length=100, unique = True)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return f"{self.name}"
    

class Tag(BaseModel):
    name = models.CharField(max_length = 100, unique = True)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return f"{self.name}"
    

class Post(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(unique = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "user_posts")
    category = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    updated_at = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return f"{self.title}"