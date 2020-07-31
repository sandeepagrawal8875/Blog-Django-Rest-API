from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Post


class PostAdmin(ModelAdmin):
    list_display = ['__str__']
    search_fields = ['title__icontains', 'text__icontains']
    list_filter = ["created_at", "update_at"]
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)