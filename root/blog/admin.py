from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register([
    Category,
    Tag,
    Post,
    Comment,
    Reaction,
    Notification
])