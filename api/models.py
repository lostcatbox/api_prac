from django.conf import settings
from django.db import models
from django.db.models import CASCADE


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name='+')
    message = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
