from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate_title(self, value):
        if 'django' not in value:
            raise ValidationError('제목에 django를 꼭 포함시켜주세요')
        return value

    def validate(self, data):
        if len(data['title'])%2==0 or len(data['content']) % 2 == 0:
            raise ValidationError('글자갯수를 홀수로만 입력해주세요')
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['pk', 'username', 'email']