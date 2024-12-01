from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from posts.models import Comment, Like, Post
from posts.permissions import IsOwnerOrReadOnly
from posts.serializers import CommentSerializer, PostSerializer

User = get_user_model()

def home_view(request):
    return HttpResponse("Здесь будет сайт!")


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        if not Like.objects.filter(post=post, user=request.user).exists():
            Like.objects.create(post=post, user=request.user)
        return Response(status=status.HTTP_200_OK)