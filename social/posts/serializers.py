from rest_framework import serializers
from posts.models import Comment, Post

"""Вывод комментариев"""
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "user", "post", "text", "created_at"]

"""Посты"""
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["id", "user", "text", "image", "created_at", "comments", "likes_count"]