
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
class PostDetailAPIVIew(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




# Create your views here.
