
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework import mixins, generics
from rest_framework import viewsets
from .serializers import PostSerializer, UserSerializer
from .models import Post
from django.shortcuts import get_object_or_404

class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer




# /post/10 => GET, PUT, DELETE 지원하기
class PostDetailAPIVIew(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


user_list = UserViewSet.as_view({
    'get': 'list',  # 호출될 함수와 호출할 함수를 지정합니다.
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
})

# Create your views here.
