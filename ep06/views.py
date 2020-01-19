from django.shortcuts import render
from ep04.models import Post
from ep04.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(
            title__icontains='두'
        )
        return qs

# Create your views here.
