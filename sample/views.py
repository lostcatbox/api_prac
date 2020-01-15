from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#class PostListAPIView(generics.ListAPIView):
    #queryset = Post.objects.all()
    #serializer_class = PostSerializer

# Create your views here.
