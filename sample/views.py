from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):     # 위에 뷰 2개,  crud모두 구현됨
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Create your views here.
