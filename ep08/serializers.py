from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')  # 추가

    class Meta:
        model = Post
        fields = ['author_username','message']