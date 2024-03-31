from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.

# User

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type', 'municipality', 'brief', 'interests',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)


# Post

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('type', 'title', 'text', 'published_by', 'created_at')

admin.site.register(Post, PostAdmin)


# Like

class LikeAdmin(admin.ModelAdmin):
    model = Like

admin.site.register(Like, LikeAdmin)


# Comment

class CommentAdmin(admin.ModelAdmin):
    model = Comment

admin.site.register(Comment, CommentAdmin)

