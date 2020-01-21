from django.shortcuts import render
from .serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Post

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(ip=self.request.META['REMOTE_ADDR'])

# Create your views here.
