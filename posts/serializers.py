from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """serialize a post"""

    def getEmail(self, obj):
        return obj.user.email

    email = serializers.SerializerMethodField("getEmail")

    class Meta:
        model = Post
        fields = ('id','email', 'title', 'text', 'created_at', 'update_at')
        read_only_fields = ('id',)

class PostImageSerializer(serializers.ModelSerializer):
    """serializer for post image"""
    class Meta:
        model = Post
        fields = ('id','image')
        read_only_fields = ('id',)