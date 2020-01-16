
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics
from .serializers import PostSerializer
from .models import Post
from django.shortcuts import get_object_or_404

class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer




# /post/10 => GET, PUT, DELETE 지원하기
class PostDetailAPIVIew(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer




# Create your views here.
