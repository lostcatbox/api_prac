from django.shortcuts import render
from ep04.models import Post
from ep04.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']
'''
    def get_queryset(self):
        qs = super().get_queryset()

        search = self.request.GET.get('search','')

        if search:
            qs = filter(title__icontains=search)
        if self.request.user.is_authenticated:  #로그인상태라면
            qs = qs.filter(
                author=self.request.user
            )
        else:
            qs = qs.none() #empty result 나옴


        return qs
'''
# Create your views here.
