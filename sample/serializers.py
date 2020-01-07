from rest_framework import serializers
from .models import Post

# ModelForm 대신에 ModelSerializer
class PostSerializer(serializers.ModelSerializer):  # form으로 생각
    class Meta:
        model = Post
        fields = '__all__'