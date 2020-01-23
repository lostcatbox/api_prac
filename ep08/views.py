from django.shortcuts import render
from .permissions import IsAuthorUpdateOrReadonly
from .serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Post

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    throttle_scope = 'contact'

    permission_classes = [
        IsAuthorUpdateOrReadonly
    ]

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            ip=self.request.META['REMOTE_ADDR']
        )



# Create your views here.
