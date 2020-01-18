from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Post
from .serializers import PostSerializer

class PostViewSet(ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# readonlymodelviewset이므로 get요청밖에없음
#아래형식으로 post_list라는 뷰함수를 만든것
post_list = PostViewSet.as_view({
    'get': 'list'
})
# Create your views here.
