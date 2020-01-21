from django.db import models

class Post(models.Model):
    message = models.CharField(max_length=25)
    ip = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
