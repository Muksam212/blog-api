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
    name = models.CharField(max_length=100, unique = True)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return f"{self.name}"


class Post(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique = True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "posts")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name = "category_post")
    tags = models.ManyToManyField(Tag, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')])
    views = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return f"{self.title}"

class Comment(BaseModel):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user_comments")
    content = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    approved = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"


class Reaction(BaseModel):
    REACTION_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'Dislike'),
        ('love', 'Love'),
        # Add more reactions as needed
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='reactions', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, related_name='reactions', on_delete=models.CASCADE, null=True, blank=True)
    reaction = models.CharField(max_length=10, choices=REACTION_CHOICES)

    class Meta:
        unique_together = ('user', 'post', 'comment')

    def __str__(self):
        target = self.post or self.comment
        return f"{self.user.username} reacted {self.reaction} on {target}"
    

class Notification(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, related_name = "user_post_notification")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True, related_name = "notes")

    def __str__(self):
        return f"Notification for {self.user.username}"